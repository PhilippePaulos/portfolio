import random
from enum import Enum

from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig


class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "top"
    DOWN = "bot"


class SnakeGame:
    def __init__(self):
        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.food_position = self._compute_food_position()
        self.current_direction = Direction.LEFT
        self.last_direction = Direction.LEFT
        self.is_collision = False
        self.score = 0

    def _compute_food_position(self):
        all_positions = [
            (row, col)
            for row in range(SnakeConfig.GRID_SIZE)
            for col in range(SnakeConfig.GRID_SIZE)
        ]
        available_positions = list(set(all_positions) - set(self.snake))
        return random.choice(available_positions)

    def get_random_direction(self):
        directions = [Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN]
        opposite = {
            Direction.RIGHT: Direction.LEFT,
            Direction.LEFT: Direction.RIGHT,
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
        }
        valid_directions = [d for d in directions if d != opposite[self.last_direction]]
        return random.choice(valid_directions)

    def move(self):
        def get_new_head(head, direction):
            head_x, head_y = head
            if direction == Direction.RIGHT:
                return head_x, head_y + 1
            elif direction == Direction.LEFT:
                return head_x, head_y - 1
            elif direction == Direction.UP:
                return head_x - 1, head_y
            else:
                return head_x + 1, head_y

        # Prevent reversing direction
        opposite = {
            Direction.RIGHT: Direction.LEFT,
            Direction.LEFT: Direction.RIGHT,
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
        }
        if self.current_direction == opposite[self.last_direction]:
            self.current_direction = self.last_direction

        new_head = get_new_head(self.snake[0], self.current_direction)

        # Check for wall collision
        if not (
            0 <= new_head[0] < SnakeConfig.GRID_SIZE
            and 0 <= new_head[1] < SnakeConfig.GRID_SIZE
        ):
            self.is_collision = True
            return

        # Check for self-collision
        if new_head in self.snake:
            self.is_collision = True
            return

        self.snake = [new_head] + self.snake

        if new_head == self.food_position:
            self.food_position = self._compute_food_position()
            self.score += 1
        else:
            self.snake.pop()

        self.last_direction = self.current_direction
