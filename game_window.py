# game_window.py
""" This module contains the functions that draw the game screen. """

import pygame
from pygame.locals import Rect
from screen_constants import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT, BLOCK_SIZE
import ui_constants

screen: pygame.Surface
""" A reference to the screen to draw on. """


grid = []


def initialise_grid_cell_colours():
    """ Resets the colours of all the cells in the grid to the default colour. """
    global grid

    default_cell_colour = 0  # COLOUR_BKG_GREY_3

    grid = []
    for x in range(BOARD_COLUMN_COUNT):
        row = []
        for y in range(BOARD_ROW_COUNT + 1):
            row.append(default_cell_colour)
        grid.append(row)


def render():
    screen.fill(ui_constants.COLOUR_BKG_GREY_1)
    _draw_grid()


def _draw_grid():
    """
    Draws the grid based on the row and column count,
    and applies the color to the grid based on the value of the grid.
    """
    for x in range(BOARD_COLUMN_COUNT):
        for y in range(BOARD_ROW_COUNT):
            pos_x = BLOCK_SIZE + (BLOCK_SIZE * x)  # add 1 to x to account for the border
            pos_y = BLOCK_SIZE + (BLOCK_SIZE * y)  # add 1 to y to account for the border
            _draw_grid_cell(pos_x, pos_y, ui_constants.BLOCK_COLOURS[grid[x][y+1]])


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
        ui_constants.COLOUR_BKG_GREY_1,
        Rect(pos_x, pos_y, BLOCK_SIZE, BLOCK_SIZE),
        1
    )


def draw_mino(grid_4x4: list, pos_x: int, pos_y: int):
    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:
                grid[pos_x + _j][pos_y + _i] = grid_4x4[_i][_j]

