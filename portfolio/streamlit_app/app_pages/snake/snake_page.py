import os
import time

import streamlit as st

from portfolio.streamlit_app.snake_ai import snake_renderer as renderer
from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig
from portfolio.streamlit_app.snake_ai.snake_game import SnakeGame

AGENTS_LIST = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]

current_dir = os.path.dirname(__file__)
snake_md_path = os.path.join(current_dir, "snake.md")
with open(snake_md_path) as f:
    GAME_DESCRIPTION = f.read()

snake_prompt_path = os.path.join(current_dir, "default_user_prompt.txt")
with open(snake_prompt_path) as f:
    DEFAULT_PROMPT = f.read()


class SnakeApp:
    def __init__(self):
        self.conf = SnakeConfig()
        if "game_1" not in st.session_state:
            st.session_state["game_1"] = SnakeGame(conf=SnakeConfig())
        if "game_2" not in st.session_state:
            st.session_state["game_2"] = SnakeGame(conf=SnakeConfig())
        self.game1: SnakeGame = st.session_state["game_1"]
        self.game2: SnakeGame = st.session_state["game_2"]

    def start_game(
        self,
        prompt_agent_1: str,
        prompt_agent_2: str,
        agent_1: str,
        agent_2: str,
        temp_1: float,
        temp_2: float,
    ):
        st.session_state["game_started"] = True
        self.game1.set_strategy_function(prompt_agent_1, agent_1, temp_1)
        self.game2.set_strategy_function(prompt_agent_2, agent_2, temp_2)

    def run(self):
        if "game_started" not in st.session_state:
            st.session_state["game_started"] = False

        if not st.session_state["game_started"]:
            self._setup_screen()
        else:
            self._game_loop()

        st.markdown(GAME_DESCRIPTION)

    def _setup_screen(self):
        col1, col2 = st.columns(2)
        with col1:
            agent1 = st.selectbox("Player 1 agent", AGENTS_LIST, key="agent1")
            temp_1 = st.slider(
                "Temperature", key="slider1", min_value=0.0, max_value=2.0, step=0.1
            )
            prompt_1 = st.text_area(
                "Provide a custom strategy or guidance to help the agent succeed in the game:",
                value=DEFAULT_PROMPT,
                key="prompt1",
            )
        with col2:
            agent2 = st.selectbox("Player 2 agent", AGENTS_LIST, key="agent2")
            temp_2 = st.slider(
                "Temperature", key="slider2", min_value=0.0, max_value=2.0, step=0.1
            )
            prompt_2 = st.text_area(
                "Provide a custom strategy or guidance to help the agent succeed in the game:",
                value=DEFAULT_PROMPT,
                key="prompt2",
            )

        # Display initial static boards
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Player 1")
            initial_board_1 = renderer.render(self.game1, self.conf)
            st.image(initial_board_1, channels="BGR")
        with col2:
            st.subheader("Player 2")
            initial_board_2 = renderer.render(self.game2, self.conf)
            st.image(initial_board_2, channels="BGR")

        st.button(
            "Play",
            on_click=self.start_game,
            args=[
                prompt_1,
                prompt_2,
                agent1,
                agent2,
                temp_1,
                temp_2,
            ],
        )

    def _game_loop(self):
        col1, col2 = st.columns(2)

        with st.container():
            with col1:
                st.subheader("Player 1")
                player_1_placeholder = st.empty()
                player_1_function_placeholder = st.expander(
                    "Player 1 Generated Function"
                )
                player_1_function_placeholder.code(
                    self.game1.generated_code, language="python"
                )
            with col2:
                st.subheader("Player 2")
                player_2_placeholder = st.empty()
                player_2_function_placeholder = st.expander(
                    "Player 2 Generated Function"
                )
                player_2_function_placeholder.code(
                    self.game2.generated_code, language="python"
                )

        while not self.game1.is_collision and not self.game2.is_collision:
            self.game1.move()
            self.game2.move()

            board_1 = renderer.render(self.game1, self.conf)
            board_2 = renderer.render(self.game2, self.conf)

            player_1_placeholder.image(board_1, channels="BGR")
            player_2_placeholder.image(board_2, channels="BGR")

            if self.game1.is_collision or self.game2.is_collision:
                st.warning("Game Over!")
                break

            time.sleep(0.2)


app = SnakeApp()
app.run()
