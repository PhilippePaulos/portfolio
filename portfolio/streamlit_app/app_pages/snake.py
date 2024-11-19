import time
import streamlit as st
import streamlit.components.v1 as components

from portfolio.streamlit_app.snake_ai.snake_config import SnakeConfig
from portfolio.streamlit_app.snake_ai.snake_game import SnakeGame, Direction
from portfolio.streamlit_app.snake_ai.snake_renderer import SnakeRenderer


class SnakeAppRandom:
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


class SnakeApp:
    """Streamlit application for running the Snake game."""

    def __init__(self):
        self.game = SnakeGame()
        self.renderer = SnakeRenderer(self.game)

    def run(self):
        st.title("Snake Game")
        st.write("Use arrow keys or WASD to control the snake.")

        if "direction" not in st.session_state:
            st.session_state["direction"] = self.game.current_direction.value

        direction = components.html(
            """
            <script>
                document.addEventListener("DOMContentLoaded", () => {
                    const keyMap = {
                        "z": "up",
                        "s": "down",
                        "q": "left",
                        "d": "right"
                    };
                
                    let currentDirection = "up";
                
                    // Ensure the window and document are focusable and focused
                    if (document.body) {
                        document.body.setAttribute("tabindex", "-1");
                        document.body.focus();
                    }
                    window.focus();  // Add this to focus the entire window
                
                    console.log("Keydown listener attached");
                
                    window.addEventListener("keydown", (event) => {
                        console.log("Key pressed:", event.key);  // Debugging key press
                        const direction = keyMap[event.key];
                        console.log(direction);
                        if (direction && direction !== currentDirection) {
                            console.log("in");
                            currentDirection = direction;
                    
                            const streamlitInput = document.getElementById("streamlit-direction");
                            streamlitInput.value = direction;
                            streamlitInput.dispatchEvent(new Event("input", { bubbles: true }));
                        }
                    });
                });

            </script>
            <input type="text" id="streamlit-direction" value="up" style="display:none;" />
            """,
            height=0,  # No visible space
        )

        # Capture the direction from JavaScript
        if direction and direction in ["up", "down", "left", "right"]:
            st.session_state["direction"] = direction
        print(st.session_state["direction"])

        new_direction = parse_direction(st.session_state["direction"])

        game_img = st.image(self.renderer.render(), channels="BGR")
        while not self.game.is_collision:
            opposite = {
                Direction.UP: Direction.DOWN,
                Direction.DOWN: Direction.UP,
                Direction.LEFT: Direction.RIGHT,
                Direction.RIGHT: Direction.LEFT,
            }
            if new_direction != opposite[self.game.last_direction]:
                self.game.current_direction = new_direction

            self.game.move()

            game_img.image(self.renderer.render(), channels="BGR")

            time.sleep(0.1)


def parse_direction(input_str):
    """Convert string direction to Direction enum."""
    direction_map = {
        "up": Direction.UP,
        "down": Direction.DOWN,
        "left": Direction.LEFT,
        "right": Direction.RIGHT,
    }
    return direction_map.get(input_str, Direction(st.session_state["direction"]))


app = SnakeApp()
app.run()
