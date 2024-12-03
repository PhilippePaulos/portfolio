import random
import textwrap

from portfolio.streamlit_app.snake_ai.llm.llm_code_generator import (
    get_strategy_from_llm,
)
from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig
from portfolio.streamlit_app.snake_ai.snake_direction import Direction


class SnakeGame:
    def __init__(self, conf: SnakeConfig):
        self.config = conf
        self.snake = [(12, 11), (11, 11), (10, 11)]
        self.food_position = self._compute_food_position()
        self.direction = Direction.DOWN
        self.last_direction = Direction.DOWN
        self.is_collision = False
        self.score = 0
        self.strategy_function = None
        self.generated_code = ""

    def _compute_food_position(self):
        all_positions = [
            (row, col)
            for row in range(self.config.GRID_SIZE)
            for col in range(self.config.GRID_SIZE)
        ]
        available_positions = list(set(all_positions) - set(self.snake))
        return random.choice(available_positions)

    def set_strategy_function(self, user_strategy: str, model: str, temperature: float):
        if user_strategy == "random":
            self.strategy_function = self.get_random_direction
        else:
            snake_code = get_strategy_from_llm(user_strategy, model, temperature)
            self.generated_code = snake_code.code
            self.strategy_function = self._create_function_from_code(snake_code.code)

    @staticmethod
    def get_random_direction(snake, food_position, direction, grid_size):
        valid_directions = [
            Direction.RIGHT,
            Direction.LEFT,
            Direction.UP,
            Direction.DOWN,
        ]
        return random.choice(valid_directions).value

    def _generate_strategy_prompt(self, user_strategy: str) -> str:
        return f"{user_strategy}\n" f"'{user_strategy}'\n\n"

    def _create_function_from_code(self, code: str):
        cleaned_code = textwrap.dedent(code)
        local_scope = {}
        exec(cleaned_code, {}, local_scope)
        return local_scope["choose_direction"]

    def move(self):
        if not self.strategy_function:
            raise ValueError("No strategy function set. Please define one first.")

        self.direction = Direction.from_str(
            self.strategy_function(
                self.snake,
                self.food_position,
                self.direction.value,
                self.config.GRID_SIZE,
            )
        )

        # Prevent reversing direction
        opposite = {
            Direction.RIGHT: Direction.LEFT,
            Direction.LEFT: Direction.RIGHT,
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
        }
        if self.direction == opposite[self.last_direction]:
            self.direction = self.last_direction

        # Compute new head position
        new_head = self._get_new_head(self.snake[0], self.direction)

        # Check for self-collision
        if new_head in self.snake:
            self.is_collision = True
            return

        # Update snake
        self.snake = [new_head] + self.snake
        if new_head == self.food_position:
            self.food_position = self._compute_food_position()
            self.score += 1
        else:
            self.snake.pop()

        self.last_direction = self.direction

    def _get_new_head(self, head, direction):
        head_x, head_y = head
        if direction == Direction.RIGHT:
            return head_x, (head_y + 1) % self.config.GRID_SIZE
        elif direction == Direction.LEFT:
            return head_x, (head_y - 1) % self.config.GRID_SIZE
        elif direction == Direction.UP:
            return (head_x - 1) % self.config.GRID_SIZE, head_y
        else:
            return (head_x + 1) % self.config.GRID_SIZE, head_y
