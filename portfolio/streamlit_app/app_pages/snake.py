import streamlit as st

from portfolio.streamlit_app.snake_ai.game import SnakeGame

broad_state = {
    "turn": 0,
    "snake": {
        "body": [(5, 2), (4, 2), (3, 2), (2, 2)],
        "dir": "R",
    },
    "food": [(7, 7)],
}

if 'game' not in st.session_state:
    st.session_state.game = SnakeGame()

st.write("# The Snake Game")

game = st.session_state.game
game_state = game.get_state()


st.markdown("")