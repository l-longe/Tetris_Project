# main.py

import pygame
import game_play_mgr
import game_window
from gamestate import GameState
from screen_constants import SCREEN_SIZE
import tetrimino_check
import game_speed


TEXT_TITLE = "TETRIS"
""" The title of the game. """


def _update_loop():
    """
    The main game loop.
    Runs until the user quits the game.
    """
    while not game_state.is_quit_triggered and not game_state.is_game_over:
        game_play_mgr.game_play_loop(game_state)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()

    game_state = GameState()

    clock = pygame.time.Clock()
    _screen = pygame.display.set_mode(SCREEN_SIZE)

    game_speed.to_normal(game_state)
    pygame.display.set_caption(TEXT_TITLE)

    tetrimino_check.game_state = game_state  # Save a reference to the game state in tetrimino_check
    game_window.screen = _screen  # Save a reference to the screen in screen_renderer
    game_window.initialise_grid_cell_colours(game_state)
    _update_loop()
