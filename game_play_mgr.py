# game_play_mgr.py
""" This module contains the game play loop. """

import pygame
from pygame.locals import QUIT, USEREVENT
import game_window
from gamestate import GameState


def game_play_loop(game_state: GameState):
    """ The main game loop. """
    for event in pygame.event.get():

        if event.type == QUIT:
            game_state.is_quit_triggered = True

        elif event.type == USEREVENT:
            _select_hardcoded_mino(game_state)

            game_window.render()
            pygame.display.update()


def _select_hardcoded_mino(game_state: GameState):
    """ Selects a hardcoded mino and where to place it on the grid. """
    game_state.mino = 1

    game_state.pos_x = 3
    game_state.pos_y = 0
    game_state.rotation = 0

    game_window.draw_mino(game_state)