# game_pause_mgr.py
""" Manages the game's behaviour when paused. """

import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, USEREVENT
import game_window
import ui_constants
from gamestate import GameState


def update_loop(game_state: GameState, screen: pygame.Surface):
    """
    Displays the pause screen and processes user inputs, including unpausing the game.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """
    for event in pygame.event.get():  # user inputs
        if event.type == QUIT:
            game_state.is_quit_triggered = True

        elif event.type == USEREVENT:
            _show_pause_text(game_state, screen)

        elif event.type == KEYDOWN:  # user presses a key
            game_window.erase_current_mino_and_ghost(game_state)

            if event.key == K_ESCAPE:
                _un_pause_game(game_state)


def _show_pause_text(game_state: GameState, screen: pygame.Surface):
    """
    Redraws the screen with the pause text and blinking text.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """
    pygame.time.set_timer(pygame.USEREVENT, 300)

    game_window.render(game_state)

    # Render the PAUSE text
    text_pause_surface = ui_constants.get_text_surface(ui_constants.TEXT_PAUSE,
                                                       font_size=30,
                                                       font_file=ui_constants.FONT_OPEN_SANS_BOLD,
                                                       color=ui_constants.COLOUR_BKG_WHITE)
    screen.blit(text_pause_surface, (43, 100))

    _display_blinking_pause_message(game_state, screen)
    pygame.display.update()


def _un_pause_game(game_state: GameState):
    """
    Unpauses the game.

    :param game_state: Current game state and variables
    """

    game_state.is_game_paused = False
    pygame.time.set_timer(pygame.USEREVENT, 1)


def _display_blinking_pause_message(game_state: GameState, screen: pygame.Surface):
    """
    Renders the blinking pause message.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """
    if game_state.is_text_blinking:
        text_continue_surface = ui_constants.get_text_surface(ui_constants.TEXT_PAUSE_ESC_CONTINUE,
                                                              color=ui_constants.COLOUR_BKG_WHITE)
        screen.blit(text_continue_surface, (40, 160))
        game_state.is_text_blinking = False

    else:
        game_state.is_text_blinking = True
