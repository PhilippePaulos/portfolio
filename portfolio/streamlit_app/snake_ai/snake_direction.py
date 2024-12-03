from enum import Enum


class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"

    @staticmethod
    def from_str(label):
        if label == "right":
            return Direction.RIGHT
        elif label == "left":
            return Direction.LEFT
        elif label == "up":
            return Direction.UP
        elif label == "down":
            return Direction.DOWN
        else:
            raise ValueError(f"Invalid direction label: {label}")
