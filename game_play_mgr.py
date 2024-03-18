# game_play_mgr.py
""" This module contains the game play loop. """

import pygame
from pygame.locals import QUIT, USEREVENT
import game_window
from gamestate import GameState
import tetrimino_check


def game_play_loop(game_state: GameState):
    """ The main game loop. """
    for event in pygame.event.get():

        if event.type == QUIT:
            game_state.is_quit_triggered = True

        elif event.type == USEREVENT:
            _draw_minos(game_state)
            pygame.display.update()


def _draw_minos(game_state: GameState):
    """
    Draws the minos on the screen.
    Steps:
    1. Draw the mino and its ghost
    2. Render the grid
    3. Erase the current mino
    4. Increase pos_y by 1, if mino is not at the bottom

    :param game_state: Current game state and variables
    """
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)
    game_window.erase_current_mino(game_state)

    # Move mino down if it is not at the bottom
    if not tetrimino_check.is_at_bottom(game_state.pos_x, game_state.pos_y, game_state.mino, game_state.rotation):
        game_state.pos_y += 1
