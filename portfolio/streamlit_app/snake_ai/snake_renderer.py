import numpy as np
import cv2

from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig
from portfolio.streamlit_app.snake_ai.snake_game import SnakeGame


class SnakeRenderer:

    def __init__(self, game: SnakeGame):
        self.game = game

    def draw_grid(self, board):
        """Draw the grid lines on the game board."""
        for i in range(SnakeConfig.GRID_SIZE + 1):
            # Draw vertical grid lines
            cv2.line(
                board,
                (i * SnakeConfig.CELL_SIZE, 0),
                (i * SnakeConfig.CELL_SIZE, SnakeConfig.WINDOW_SIZE),
                SnakeConfig.GRID_COLOR,
                1,
            )
            # Draw horizontal grid lines
            cv2.line(
                board,
                (0, i * SnakeConfig.CELL_SIZE),
                (SnakeConfig.WINDOW_SIZE, i * SnakeConfig.CELL_SIZE),
                SnakeConfig.GRID_COLOR,
                1,
            )

    def draw_snake(self, board):
        for x, y in self.game.snake:
            top_left = (y * SnakeConfig.CELL_SIZE, x * SnakeConfig.CELL_SIZE)
            bottom_right = (
                (y + 1) * SnakeConfig.CELL_SIZE,
                (x + 1) * SnakeConfig.CELL_SIZE,
            )
            cv2.rectangle(board, top_left, bottom_right, SnakeConfig.SNAKE_COLOR, -1)

    def draw_food(self, board):
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

    def draw_game_board(self):
        board = np.zeros(
            (SnakeConfig.WINDOW_SIZE, SnakeConfig.WINDOW_SIZE, 3), dtype=np.uint8
        )
        board[:] = SnakeConfig.BG_COLOR

        # Draw components
        self.draw_grid(board)
        self.draw_snake(board)
        self.draw_food(board)

        return board

    def draw_score_area(self, canvas):
        """Draw the score area at the top of the canvas."""
        score_bg_color = (20, 20, 20)
        cv2.rectangle(
            canvas,
            (0, 0),
            (SnakeConfig.WINDOW_SIZE, 60),
            score_bg_color,
            -1,
        )

        font = cv2.FONT_HERSHEY_SIMPLEX
        text_color = (255, 255, 255)
        cv2.putText(
            canvas,
            f"Score: {self.game.score}",
            (20, 40),
            font,
            1.5,
            text_color,
            2,
            cv2.LINE_AA,
        )

    def draw_game_over_overlay(self, canvas):
        overlay_text = "GAME OVER"
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_color = (0, 0, 255)  # Red color
        font_scale = 2
        thickness = 3

        text_size = cv2.getTextSize(overlay_text, font, font_scale, thickness)[0]
        text_x = (SnakeConfig.WINDOW_SIZE - text_size[0]) // 2
        text_y = (SnakeConfig.WINDOW_SIZE + text_size[1]) // 2 + 60

        cv2.putText(
            canvas,
            overlay_text,
            (text_x, text_y),
            font,
            font_scale,
            text_color,
            thickness,
            cv2.LINE_AA,
        )

    def render(self):
        canvas_height = SnakeConfig.WINDOW_SIZE + 60
        canvas = np.zeros((canvas_height, SnakeConfig.WINDOW_SIZE, 3), dtype=np.uint8)
        canvas[:] = SnakeConfig.BG_COLOR

        self.draw_score_area(canvas)

        board = self.draw_game_board()
        canvas[60:, :] = board

        if self.game.is_collision:
            self.draw_game_over_overlay(canvas)

        return canvas
