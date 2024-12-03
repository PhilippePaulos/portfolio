You are tasked with generating a Python function to control a snake in a grid-based game. Follow these strict requirements and provide only the raw Python function code.
Function Signature

def choose_direction(snake: list, food: tuple, current_direction: str, grid_size: int) -> str:
    snake: List of (x, y) tuples representing the snake's body (head is the first element).
    food: Tuple (x, y) representing the food position.
    current_direction: String ('up', 'down', 'left', 'right') representing the current direction.
    grid_size: An integer representing the grid size (e.g., 20 for a 20x20 grid).

Rules
    Provide only the Python function code.
        Do not include any explanations, comments, or additional text.
        Do not include markdown formatting (e.g., ``` or ```python).
    The function must:
        Be named choose_direction.
        Take the required parameters (snake, food, current_direction, and grid_size).
        Return one of 'up', 'down', 'left', or 'right'.
        Avoid collisions with the snake's body.
        Handle grid wrapping correctly for both rows and columns.
        Use the Manhattan distance heuristic to optimize movement toward the food.
        Always handle edge cases gracefully, such as when no valid moves exist.
    Ensure the function is valid Python code, fully self-contained, and can execute without errors.

You will have to adapt your strategy and code by respecting the user's prompt.