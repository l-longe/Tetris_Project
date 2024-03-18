# tetrimino_check.py
# """ This module contains checks and validations specifically for Tetriminos. """

import tetriminos
from gamestate import GameState

game_state: GameState
""" A reference to the current game state and variables. """


def is_at_bottom(x, y, mino, r):
    """
    Returns true if mino is at the bottom of the grid.

    :param mino: The specified mino
    :param x: The x position of the specified mino
    :param y: The y position of the specified mino
    :param r: The rotation of the specified mino
    """

    # Choose the correct Tetrimino instance based on _mino value
    tetrimino = tetriminos.get(mino)

    # Get the grid based on rotation
    grid = tetrimino.get_rotated_grid(r)
    """ The 4x4 grid of the tetrimino based on the rotation. """

    for _i in range(4):
        for _j in range(4):
            if grid[_i][_j] != 0:
                if (y + _i + 1) > 20:
                    return True  # The mino is at the bottom of the grid
    return False
