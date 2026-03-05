# screen_constants.py
""" This module contains the constants used to draw the game screen. """

from pygame.locals import Rect

BLOCK_SIZE = 17
""" The size (height & width) of a single block in pixels. """

BORDER = BLOCK_SIZE * 2  # 34 or (17 * 2)
""" The width of the border around the board in pixels. """

BOARD_COLUMN_COUNT = 10
""" The number of columns in the board. """
BOARD_ROW_COUNT = 20
""" The number of rows in the board. """

SIDE_BAR_POS_Y = 0
""" The y position of the sidebar in pixels. """
SIDE_BAR_POS_X = BLOCK_SIZE * BOARD_COLUMN_COUNT + BORDER  # 204 or (17 * 10 + 34)
""" The x position of the sidebar in pixels. """

SIDE_BAR_WIDTH = (BLOCK_SIZE * 4) + (BLOCK_SIZE * 2)  # 102 or (17 * 4 + 17 * 2)
""" The width of the sidebar in pixels. """
SIDE_BAR_HEIGHT = BLOCK_SIZE * BOARD_ROW_COUNT + BORDER  # 374 or (17 * 20 + 34)
""" The height of the sidebar in pixels. """
SIDE_BAR_RECT: Rect = Rect(SIDE_BAR_POS_X, SIDE_BAR_POS_Y, SIDE_BAR_WIDTH, SIDE_BAR_HEIGHT)
""" The rectangle that represents the sidebar. \n
    The sidebar is the area on the right of the board. \n
    204 + 96 = 300, which is the width of the screen. \n
    374 is the height of the screen. """

SCREEN_WIDTH = 300
""" The width of the screen in pixels. """

SCREEN_HEIGHT = 374
""" The height of the screen in pixels. """

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
""" The size of the screen in pixels. """
