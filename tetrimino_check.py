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


def is_at_left_edge(x, y, _mino, r):
    """
    Returns true if mino is at the left edge.

    :param x: The x position of the mino
    :param y: The y position of the mino
    :param _mino: The mino
    :param r: The rotation of the mino
    """

    # Choose the correct Tetrimino instance based on _mino value
    tetrimino = tetriminos.get(_mino)

    # Get the grid based on rotation
    grid_4x4 = tetrimino.get_rotated_grid(r)
    """ The 4x4 grid of the tetrimino based on the rotation. """

    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:
                if (x + _j - 1) < 0:
                    return True
                elif game_state.grid[x + _j - 1][y + _i] != 0:
                    return True

    return False


def is_at_right_edge(x, y, _mino, r):
    """
    Returns true if mino is at the right edge.

    :param x: The x position of the mino
    :param y: The y position of the mino
    :param _mino: The mino
    :param r: The rotation of the mino
    """

    # Choose the correct Tetrimino instance based on _mino value
    tetrimino = tetriminos.get(_mino)

    # Get the grid based on rotation
    grid = tetrimino.get_rotated_grid(r)
    """ The 4x4 grid of the tetrimino based on the rotation. """

    for _i in range(4):
        for _j in range(4):
            if grid[_i][_j] != 0:  # If the cell is not empty
                if (x + _j + 1) > 9:
                    return True
                elif game_state.grid[x + _j + 1][y + _i] != 0:
                    return True

    return False
