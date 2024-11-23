import cv2
import numpy as np

from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig
from portfolio.streamlit_app.snake_ai.snake_game import SnakeGame


def render(game: SnakeGame, config: SnakeConfig) -> np.ndarray:
    window_size = config.WINDOW_SIZE
    cell_size = config.CELL_SIZE
    colors = {
        "background": config.BG_COLOR,
        "grid": config.GRID_COLOR,
        "snake_body": config.SNAKE_BODY_COLOR,
        "snake_head": config.SNAKE_EYES_COLOR,
        "food": config.FOOD_COLOR,
        "score_bg": (20, 20, 20),
        "score_text": (255, 255, 255),
    }

    canvas_height = window_size + 60  # Include score area
    board = np.zeros((canvas_height, window_size, 3), dtype=np.uint8)
    board[:] = colors["background"]

    _draw_score_area(
        board, window_size, game.score, colors["score_text"], colors["score_bg"]
    )

    game_board = _create_board(window_size, colors["background"])
    _draw_grid(game_board, config.GRID_SIZE, cell_size, colors["grid"])
    _draw_snake(
        game_board,
        game.snake,
        cell_size,
        colors["snake_body"],
        colors["snake_head"],
        game.direction.value,
    )
    _draw_food(game_board, game.food_position, cell_size, colors["food"])

    board[60:, :] = game_board

    if game.is_collision:
        _draw_game_over_overlay(board, window_size)

    return board


def _create_board(window_size, bg_color):
    board = np.zeros((window_size, window_size, 3), dtype=np.uint8)
    board[:] = bg_color
    return board


def _draw_grid(board, grid_size, cell_size, grid_color):
    for i in range(grid_size + 1):
        # Vertical lines
        cv2.line(
            board,
            (i * cell_size, 0),
            (i * cell_size, board.shape[1]),
            grid_color,
            1,
        )
        # Horizontal lines
        cv2.line(
            board,
            (0, i * cell_size),
            (board.shape[0], i * cell_size),
            grid_color,
            1,
        )


def _draw_snake(board, snake, cell_size, snake_body_color, snake_head_color, direction):
    for index, (x, y) in enumerate(snake):
        top_left = (y * cell_size, x * cell_size)
        bottom_right = ((y + 1) * cell_size, (x + 1) * cell_size)

        # Draw the body of the snake
        cv2.rectangle(board, top_left, bottom_right, snake_body_color, -1)

        if index == 0:  # Draw the head with eyes
            head_center_x = (top_left[0] + bottom_right[0]) // 2
            head_center_y = (top_left[1] + bottom_right[1]) // 2
            eye_offset = cell_size // 4
            eye_radius = cell_size // 10

            if direction == "up":
                left_eye = (head_center_x - eye_offset, head_center_y - eye_offset)
                right_eye = (head_center_x + eye_offset, head_center_y - eye_offset)
            elif direction == "down":
                left_eye = (head_center_x - eye_offset, head_center_y + eye_offset)
                right_eye = (head_center_x + eye_offset, head_center_y + eye_offset)
            elif direction == "left":
                left_eye = (head_center_x - eye_offset, head_center_y - eye_offset)
                right_eye = (head_center_x - eye_offset, head_center_y + eye_offset)
            elif direction == "right":
                left_eye = (head_center_x + eye_offset, head_center_y - eye_offset)
                right_eye = (head_center_x + eye_offset, head_center_y + eye_offset)
            else:
                raise ValueError(f"Unexpected direction: {direction}")

            # Draw the eyes
            cv2.circle(board, left_eye, eye_radius, snake_head_color, -1)
            cv2.circle(board, right_eye, eye_radius, snake_head_color, -1)


def _draw_food(board, food_position, cell_size, food_color):
    top_left = (food_position[1] * cell_size, food_position[0] * cell_size)
    bottom_right = (
        (food_position[1] + 1) * cell_size,
        (food_position[0] + 1) * cell_size,
    )
    cv2.rectangle(board, top_left, bottom_right, food_color, -1)


def _draw_score_area(board, window_size, score, score_color, bg_color):
    score_area_height = 60
    cv2.rectangle(
        board,
        (0, 0),
        (window_size, score_area_height),
        bg_color,
        -1,
    )

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        board,
        f"Score: {score}",
        (20, 40),
        font,
        1.5,
        score_color,
        2,
        cv2.LINE_AA,
    )


def _draw_game_over_overlay(board, window_size):
    overlay_text = "GAME OVER"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_color = (0, 0, 255)  # Red
    font_scale = 2
    thickness = 3

    text_size = cv2.getTextSize(overlay_text, font, font_scale, thickness)[0]
    text_x = (window_size - text_size[0]) // 2
    text_y = (window_size + text_size[1]) // 2

    cv2.putText(
        board,
        overlay_text,
        (text_x, text_y),
        font,
        font_scale,
        text_color,
        thickness,
        cv2.LINE_AA,
    )
