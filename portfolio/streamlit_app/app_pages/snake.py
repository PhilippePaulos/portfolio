import time
import streamlit as st

from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig
from portfolio.streamlit_app.snake_ai.snake_game import SnakeGame
from portfolio.streamlit_app.snake_ai.snake_renderer import SnakeRenderer


class SnakeApp:
    def __init__(self):
        self.game = SnakeGame()
        self.renderer = SnakeRenderer(self.game)

    def run(self):
        game_img = st.image(self.renderer.render(), channels="BGR")

        while not self.game.is_collision:
            self.game.current_direction = self.game.get_random_direction()
            self.game.move()
            board = self.renderer.render()
            game_img.image(board, channels="BGR")
            if self.game.is_collision:
                break
            time.sleep(SnakeConfig.REFRESH_TIME)


app = SnakeApp()
app.run()
