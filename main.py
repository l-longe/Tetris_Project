# main.py

import pygame
from pygame.locals import QUIT, USEREVENT
import game_window
from gamestate import GameState
from screen_constants import SCREEN_SIZE

FRAME_RATE = 30

TEXT_TITLE = "TETRIS"
""" The title of the game. """


def _select_hardcoded_mino():
    """ Selects a hardcoded mino and where to place it on the grid. """
    game_state.mino = 1

    game_state.pos_x = 3
    game_state.pos_y = 0
    game_state.rotation = 0

    game_window.draw_mino(game_state)


def game_play_loop():
    """ The main game loop. """
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state.is_quit_triggered = True

        elif event.type == USEREVENT:
            _select_hardcoded_mino()

        game_window.render()
        pygame.display.update()


def _update_loop():
    """
    The main game loop.
    Runs until the user quits the game.
    """
    while not game_state.is_quit_triggered:
        game_play_loop()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()

    game_state = GameState()

    clock = pygame.time.Clock()
    _screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.time.set_timer(pygame.USEREVENT, FRAME_RATE * 10)
    pygame.display.set_caption(TEXT_TITLE)

    game_window.screen = _screen  # Save a reference to the screen in screen_renderer
    game_window.initialise_grid_cell_colours()

    _update_loop()