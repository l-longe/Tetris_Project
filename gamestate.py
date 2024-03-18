# gamestate.py
"""Holds the game data that represents the state of the game."""


class GameState:
    """
    Represents the current state of the game, including all variables that change as the game progresses.

    Attributes:
        mino (int): The offset index of the current falling mino.

        pos_x (int): The horizontal position (column) of the current falling mino.
        pos_y (int): The vertical position (row) of the current falling mino.
        rotation (int): The rotation state of the current falling mino. 0=0°, 1=90°, 2=180°, 3=270°

        is_quit_triggered (bool): True when a quit action is triggered by the user.
        grid (list): The grid representing the Tetris board. \n
            It is the grid on which the tetriminos are drawn and manipulated.
    """

    def __init__(self):
        self.mino_4x4 = []
        self.mino: int = 1

        self.pos_x: int = 3
        self.pos_y: int = 0
        self.rotation: int = 0

        self.is_quit_triggered: bool = False

        self.grid = []
