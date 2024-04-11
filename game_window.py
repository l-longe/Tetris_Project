# game_window.py
""" This module contains the functions that draw the game screen. """

import pygame
from pygame.locals import Rect

import tetrimino_check
import tetriminos
from gamestate import GameState
from screen_constants import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT, BLOCK_SIZE, SIDE_BAR_RECT
import ui_constants

screen: pygame.Surface
""" A reference to the screen to draw on. """


def initialise_grid_cell_colours(game_state: GameState):
    """ Resets the colours of all the cells in the grid to the default colour. """
    default_cell_colour = 0  # COLOUR_BKG_GREY_3

    game_state.grid = []
    for x in range(BOARD_COLUMN_COUNT):
        row = []
        for y in range(BOARD_ROW_COUNT + 1):
            row.append(default_cell_colour)
        game_state.grid.append(row)


def render(game_state: GameState):
    """
    Renders the game. \n
    Draws the grid, borders, sidebar and all the elements in it.

    :param game_state: Current game state and variables
    """

    screen.fill(ui_constants.COLOUR_BKG_GREY_1)

    _draw_grid(game_state)
    _draw_sidebar()


def _draw_grid(game_state: GameState):
    """
    Draws the grid based on the row and column count,
    and applies the color to the grid based on the value of the grid.
    """
    for x in range(BOARD_COLUMN_COUNT):
        for y in range(BOARD_ROW_COUNT):
            pos_x = BLOCK_SIZE + (BLOCK_SIZE * x)  # add 1 to x to account for the border
            pos_y = BLOCK_SIZE + (BLOCK_SIZE * y)  # add 1 to y to account for the border
            _draw_grid_cell(pos_x, pos_y, ui_constants.BLOCK_COLOURS[game_state.grid[x][y+1]])


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


def draw_current_mino_and_ghost(game_state: GameState):
    """ Draws the current falling tetrimino, and it's ghost on the board.

    :param game_state: Current game state and variables
    """

    # Choose the correct Tetrimino based on mino value
    mino = tetriminos.get(game_state.mino)

    # Get the tetrimino's 4x4 grid based on it's rotation
    grid_4x4: list = mino.get_rotated_grid(game_state.rotation)

    # Set ghost position
    gx, gy = game_state.pos_x, game_state.pos_y
    while not tetrimino_check.is_at_bottom(gx, gy, game_state.mino, game_state.rotation):
        gy += 1  # place the ghost at the lowest possible position

    # Draw ghost
    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:
                game_state.grid[gx + _j][gy + _i] = 8

    # Draw the current mino
    pos_x: int = game_state.pos_x
    pos_y: int = game_state.pos_y
    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:
                game_state.grid[pos_x + _j][pos_y + _i] = grid_4x4[_i][_j]


def erase_current_mino_and_ghost(game_state: GameState):
    """
    Removes the current falling tetrimino and it's ghost from the board.

    :param game_state: Current game state and variables
    """

    # Choose the correct Tetrimino instance based on _mino value
    mino = tetriminos.get(game_state.mino)

    # Get the tetrimino's 4x4 grid based on it's rotation
    grid_4x4: list = mino.get_rotated_grid(game_state.rotation)

    # Erase ghost
    for _i in range(10):
        for _j in range(21):
            if game_state.grid[_i][_j] == 8:  # Ghost cells are marked with 8
                game_state.grid[_i][_j] = 0

    # Erase mino
    pos_x: int = game_state.pos_x
    pos_y: int = game_state.pos_y
    for _i in range(4):
        for _j in range(4):
            if grid_4x4[_i][_j] != 0:  # if the cell is not empty
                game_state.grid[pos_x + _j][pos_y + _i] = 0


def _draw_sidebar():
    """ Draws the sidebar on the right of the board. """
    pygame.draw.rect(
        screen,
        ui_constants.COLOUR_BKG_WHITE,
        SIDE_BAR_RECT
    )
