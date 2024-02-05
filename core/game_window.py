# game_window.py
""" This module contains the functions that draw the game screen. """

import pygame
from pygame.locals import Rect
from screen_constants import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT, BLOCK_SIZE, SCREEN_SIZE
from ui_constants import COLOUR_BKG_GREY_1, COLOUR_BKG_GREY_3

screen: pygame.Surface
""" A reference to the screen to draw on. """


def draw_grid():
    for x in range(BOARD_COLUMN_COUNT):
        for y in range(BOARD_ROW_COUNT):
            pos_x = BLOCK_SIZE + (BLOCK_SIZE * x)  # add 1 to x to account for the border
            pos_y = BLOCK_SIZE + (BLOCK_SIZE * y)  # add 1 to y to account for the border
            _draw_grid_cell(pos_x, pos_y, COLOUR_BKG_GREY_3)


def _draw_grid_cell(pos_x, pos_y, color):
    """
    Draw a cell at the given position with the given color.

    :param pos_x: The x position of the cell
    :param pos_y: The y position of the cell
    :param color: The color of the cell
    """

    # Draw the cell
    pygame.draw.rect(
        screen,
        color,
        Rect(pos_x, pos_y, BLOCK_SIZE, BLOCK_SIZE)
    )

    # Draw the border of the cell
    pygame.draw.rect(
        screen,
        COLOUR_BKG_GREY_1,
        Rect(pos_x, pos_y, BLOCK_SIZE, BLOCK_SIZE),
        1
    )
