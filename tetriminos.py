# tetriminos.py
""" This module contains the tetrimino class and the 7 standard tetrimino-shapes. """


class _Tetrimino:
    rotation_1: list
    """ The first rotation of the tetrimino. """

    rotation_2: list
    """ The second rotation of the tetrimino. """

    rotation_3: list
    """ The third rotation of the tetrimino."""

    rotation_4: list
    """ The fourth rotation of the tetrimino. """

    def __init__(self, _name: str):
        self.name = _name

    def get_rotated_grid(self, r: int) -> list:
        """
        Returns the 4x4 grid of the tetrimino based on the rotation.

        :param r: A 0-indexed rotation of the tetrimino.
        :return: The rotated grid for the tetrimino.
        """

        r += 1  # Because the rotations are 1-indexed
        if r == 1:
            return self.rotation_1
        elif r == 2:
            return self.rotation_2
        elif r == 3:
            return self.rotation_3
        elif r == 4:
            return self.rotation_4


I: _Tetrimino = _Tetrimino("I")
I.rotation_1 = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
I.rotation_2 = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]
I.rotation_3 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]
I.rotation_4 = [
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]


J: _Tetrimino = _Tetrimino("J")
J.rotation_1 = [
    [2, 0, 0, 0],
    [2, 2, 2, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
J.rotation_2 = [
    [0, 2, 2, 0],
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
]
J.rotation_3 = [
    [0, 0, 0, 0],
    [2, 2, 2, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0]
]
J.rotation_4 = [
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [2, 2, 0, 0],
    [0, 0, 0, 0]
]


L: _Tetrimino = _Tetrimino("L")
L.rotation_1 = [
    [0, 0, 3, 0],
    [3, 3, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
L.rotation_2 = [
    [0, 3, 0, 0],
    [0, 3, 0, 0],
    [0, 3, 3, 0],
    [0, 0, 0, 0]
]
L.rotation_3 = [
    [0, 0, 0, 0],
    [3, 3, 3, 0],
    [3, 0, 0, 0],
    [0, 0, 0, 0]
]
L.rotation_4 = [
    [3, 3, 0, 0],
    [0, 3, 0, 0],
    [0, 3, 0, 0],
    [0, 0, 0, 0]
]


O: _Tetrimino = _Tetrimino("O")
O.rotation_1 = [
    [0, 4, 4, 0],
    [0, 4, 4, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
O.rotation_2 = [
    [0, 4, 4, 0],
    [0, 4, 4, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
O.rotation_3 = [
    [0, 4, 4, 0],
    [0, 4, 4, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
O.rotation_4 = [
    [0, 4, 4, 0],
    [0, 4, 4, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


S: _Tetrimino = _Tetrimino("S")
S.rotation_1 = [
    [0, 5, 5, 0],
    [5, 5, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
S.rotation_2 = [
    [0, 5, 0, 0],
    [0, 5, 5, 0],
    [0, 0, 5, 0],
    [0, 0, 0, 0]
]
S.rotation_3 = [
    [0, 0, 0, 0],
    [0, 5, 5, 0],
    [5, 5, 0, 0],
    [0, 0, 0, 0]
]
S.rotation_4 = [
    [5, 0, 0, 0],
    [5, 5, 0, 0],
    [0, 5, 0, 0],
    [0, 0, 0, 0]
]


T: _Tetrimino = _Tetrimino("T")
T.rotation_1 = [
    [0, 6, 0, 0],
    [6, 6, 6, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
T.rotation_2 = [
    [0, 6, 0, 0],
    [0, 6, 6, 0],
    [0, 6, 0, 0],
    [0, 0, 0, 0]
]
T_rotation_3 = [
    [0, 0, 0, 0],
    [6, 6, 6, 0],
    [0, 6, 0, 0],
    [0, 0, 0, 0]
]
T.rotation_4 = [
    [0, 6, 0, 0],
    [6, 6, 0, 0],
    [0, 6, 0, 0],
    [0, 0, 0, 0]
]


Z: _Tetrimino = _Tetrimino("Z")
Z.rotation_1 = [
    [7, 7, 0, 0],
    [0, 7, 7, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
Z.rotation_2 = [
    [0, 0, 7, 0],
    [0, 7, 7, 0],
    [0, 7, 0, 0],
    [0, 0, 0, 0]
]
Z.rotation_3 = [
    [0, 0, 0, 0],
    [7, 7, 0, 0],
    [0, 7, 7, 0],
    [0, 0, 0, 0]
]
Z.rotation_4 = [
    [0, 7, 0, 0],
    [7, 7, 0, 0],
    [7, 0, 0, 0],
    [0, 0, 0, 0]
]


_MAP = [I, J, L, O, S, T, Z]
""" A private list of all the tetrimino shapes. """


def get(offset: int) -> _Tetrimino:
    """
    Returns the tetrimino based on its offset index.

    - get(1) returns the I tetrimino,
    - get(2) returns the J tetrimino, etc.

    The numbers are offset by 1
    so that they correspond to the colours in the ui_constants.BLOCK_COLOURS list.

    :param offset: An offset index of the tetrimino in the _MAP list.
    :return: The tetrimino.
    """
    return _MAP[offset - 1]
