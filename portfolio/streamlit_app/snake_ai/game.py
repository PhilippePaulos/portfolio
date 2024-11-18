import random


class SnakeGame:
    def __init__(self, grid_size=10):
        self.started = True
        self.grid_size = grid_size
        self.snake = []
        self.direction = (0, 1)
        self.food = (0, 0)

    def start(self):
        self.snake = [(0, 0)]
        self.spawn_food()
        self.started = True

    def reset(self):
        self.started = False

    def spawn_food(self):
        self.food = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))

    def change_direction(self, direction):
        self.direction = direction

    def step(self):
        head_x, head_y = self.snake[0]
        print(head_x, head_y)
        dir_x, dir_y = self.direction
        print(dir_x, dir_y)
        new_head = (head_x + dir_x, head_y + dir_y)
        print(new_head)

        if new_head in self.snake or not (0 <= new_head[0] < self.grid_size and 0 <= new_head[1] < self.grid_size):
            # Game over
            return False

        self.snake = [new_head] + self.snake[:-1]

        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.spawn_food()

        return True

    def get_score(self) -> int:
        return len(self.snake) - 1

    def get_state(self):
        return {
            'snake': self.snake,
            'food': self.food,
            'grid_size': self.grid_size,
            'score': self.get_score(),
        }
