# gamestate.py
"""Holds the game data that represents the state of the game."""
from random import randint


class GameState:
    """
    Represents the current state of the game, including all variables that change as the game progresses.

    Attributes:

        pos_x (int): The horizontal position (column) of the current falling mino.
        pos_y (int): The vertical position (row) of the current falling mino.
        rotation (int): The rotation state of the current falling mino. 0=0°, 1=90°, 2=180°, 3=270°

        mino (int): The offset index of the current falling mino.
        next_mino (int): The type of the next mino to fall.

        held_mino (int): The type of the mino that is currently on hold. \n
                    -1 means no mino is on hold.
        is_holding_mino (bool): True if the player is currently holding a mino.

        is_quit_triggered (bool): True when a quit action is triggered by the user.

        in_hard_drop (bool): True when the current mino is being hard (fast) dropped.
        post_landing_delay (int): A short delay after a mino lands, and before the next mino starts falling. \n
            It does not apply if the current mino is hard dropped.
            It allows the user to move the mino left or right, just after it lands.


        grid (list): The grid representing the Tetris board. \n
            It is the grid on which the tetriminos are drawn and manipulated.

        frame_rate (int): The frame rate for the game's update speed. \n
            A higher value means a slower update speed.
    """

    def __init__(self):

        self.pos_x: int = 3
        self.pos_y: int = 0
        self.rotation: int = 0

        self.mino: int = randint(1, 7)
        self.next_mino: int = randint(1, 7)

        self.held_mino: int = -1
        self.is_holding_mino: bool = False

        self.is_quit_triggered: bool = False

        self.in_hard_drop: bool = False
        self.post_landing_delay: int = 0

        self.grid = []

        self.frame_rate = 30
