import numpy as np
import cv2
from portfolio.streamlit_app.snake_ai.snake_game import SnakeGame, SnakeConfig


class SnakeRenderer:
    """Class responsible for rendering the Snake game."""

    def __init__(self, game: SnakeGame):
        self.game = game

    def draw_board(self):
        """Draw the game board with the snake and food."""
        board = np.zeros(
            (SnakeConfig.WINDOW_SIZE, SnakeConfig.WINDOW_SIZE, 3), dtype=np.uint8
        )
        board[:] = SnakeConfig.BG_COLOR

        # Draw grid lines
        for i in range(SnakeConfig.GRID_SIZE + 1):
            cv2.line(
                board,
                (i * SnakeConfig.CELL_SIZE, 0),
                (i * SnakeConfig.CELL_SIZE, SnakeConfig.WINDOW_SIZE),
                SnakeConfig.GRID_COLOR,
                1,
            )
            cv2.line(
                board,
                (0, i * SnakeConfig.CELL_SIZE),
                (SnakeConfig.WINDOW_SIZE, i * SnakeConfig.CELL_SIZE),
                SnakeConfig.GRID_COLOR,
                1,
            )

        # Draw the snake
        for x, y in self.game.snake:
            top_left = (y * SnakeConfig.CELL_SIZE, x * SnakeConfig.CELL_SIZE)
            bottom_right = (
                (y + 1) * SnakeConfig.CELL_SIZE,
                (x + 1) * SnakeConfig.CELL_SIZE,
            )
            cv2.rectangle(board, top_left, bottom_right, SnakeConfig.SNAKE_COLOR, -1)

        # Draw the food
        food_top_left = (
            self.game.food_position[1] * SnakeConfig.CELL_SIZE,
            self.game.food_position[0] * SnakeConfig.CELL_SIZE,
        )
        food_bottom_right = (
            (self.game.food_position[1] + 1) * SnakeConfig.CELL_SIZE,
            (self.game.food_position[0] + 1) * SnakeConfig.CELL_SIZE,
        )
        cv2.rectangle(
            board, food_top_left, food_bottom_right, SnakeConfig.FOOD_COLOR, -1
        )

        return board

    def render(self):
        return self.draw_board()
