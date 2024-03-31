# gamestate.py
"""Holds the game data that represents the state of the game."""
from random import randint


class GameState:
    """
    Represents the current state of the game, including all variables that change as the game progresses.

    Attributes:
        mino (int): The offset index of the current falling mino.
        next_mino (int): The type of the next mino to fall.

        pos_x (int): The horizontal position (column) of the current falling mino.
        pos_y (int): The vertical position (row) of the current falling mino.
        rotation (int): The rotation state of the current falling mino. 0=0°, 1=90°, 2=180°, 3=270°

        is_quit_triggered (bool): True when a quit action is triggered by the user.

        in_hard_drop (bool): True when the current mino is being hard (fast) dropped.
        post_landing_delay (int): A short delay after a mino lands, and before the next mino starts falling. \n
            It does not apply if the current mino is hard dropped.
            It allows the user to move the mino left or right, just after it lands.

        grid (list): The grid representing the Tetris board. \n
            It is the grid on which the tetriminos are drawn and manipulated.
    """

    def __init__(self):
        self.mino: int = randint(1, 7)
        self.next_mino: int = randint(1, 7)

        self.pos_x: int = 3
        self.pos_y: int = 0
        self.rotation: int = 0

        self.is_quit_triggered: bool = False

        self.in_hard_drop: bool = False
        self.post_landing_delay: int = 0

        self.grid = []
