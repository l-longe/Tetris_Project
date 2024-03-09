# gamestate.py
"""Holds the game data that represents the state of the game."""


class GameState:
    """
    Represents the current state of the game, including all variables that change as the game progresses.

    Attributes:
        mino_4x4 (list): A nested list representing how to draw and paint the current mino.

        pos_x (int): The horizontal position (column) of the current falling mino.
        pos_y (int): The vertical position (row) of the current falling mino.
    """

    def __init__(self):
        self.mino_4x4 = []

        self.pos_x: int = 0
        self.pos_y: int = 0
