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


def can_rotate_right(x, y, _mino, r):
    """
    Returns true if turning right is possible.

    :param x: The x position of the mino
    :param y: The y position of the mino
    :param _mino: The mino
    :param r: The rotation of the mino
    """

    # Choose the correct Tetrimino instance based on _mino value
    tetrimino = tetriminos.get(_mino)

    next_rotation: int = r + 1 if r < 3 else 0  # Rotations go from 0 to 3

    # Get the grid based on rotation
    grid_4x4 = tetrimino.get_rotated_grid(next_rotation)
    """ The 4x4 grid of the tetrimino based on the rotation. """

    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:
                if (x + _j) < 0 or (x + _j) > 9 or (y + _i) < 0 or (y + _i) > 20:
                    return False
                elif game_state.grid[x + _j][y + _i] != 0:
                    return False

    return True


def can_rotate_left(x, y, _mino, r):
    """
    Returns true if turning left is possible.

    :param x: The x position of the mino
    :param y: The y position of the mino
    :param _mino: The mino
    :param r: The rotation of the mino
    """

    # Choose the correct Tetrimino instance based on _mino value
    tetrimino = tetriminos.get(_mino)

    prev_rotation = r - 1 if r > 0 else 3  # Rotations go from 0 to 3

    # Get the grid based on rotation
    grid_4x4 = tetrimino.get_rotated_grid(prev_rotation)
    """ The 4x4 grid of the tetrimino based on the rotation. """

    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:
                if (x + _j) < 0 or (x + _j) > 9 or (y + _i) < 0 or (y + _i) > 20:
                    return False
                elif game_state.grid[x + _j][y + _i] != 0:
                    return False

    return True


def can_fit_in_grid(_mino):
    """
    Returns True if there is enough space to add this mino to the grid.

    :param _mino: The mino
    """

    # Choose the correct Tetrimino instance based on _mino value
    tetrimino = tetriminos.get(_mino)

    grid_4x4 = tetrimino.rotation_1  # Always checking the first rotation
    """ The 4x4 grid of the tetrimino based on the rotation. """

    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0 and game_state.grid[3 + _j][_i] != 0:
                return False

    return True
