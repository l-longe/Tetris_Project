# game_over_mgr.py
""" Manages all the game over related activities, including drawing the screen and processing inputs."""

import pygame
from pygame.locals import QUIT, USEREVENT
import game_window
import ui_constants
from gamestate import GameState


def update_loop(game_state: GameState, screen: pygame.Surface):
    """
    Draws the game over text on top of the game window.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state.is_quit_triggered = True

        elif event.type == USEREVENT:
            _show_game_over_text(game_state, screen)


def _show_game_over_text(game_state: GameState, screen: pygame.Surface):
    """
    Displays the game over screen and the names of the players.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """
    pygame.time.set_timer(pygame.USEREVENT, 300)

    # Render the grid and all the tetriminos
    game_window.render(game_state)

    # Draw GAME OVER text
    txt_game_surface = ui_constants.get_text_surface(ui_constants.TEXT_GAME_OVER[0],
                                                     font_size=30,
                                                     font_file=ui_constants.FONT_OPEN_SANS_BOLD,
                                                     color=ui_constants.COLOUR_BKG_WHITE)
    txt_over_surface = ui_constants.get_text_surface(ui_constants.TEXT_GAME_OVER[1],
                                                     font_size=30,
                                                     font_file=ui_constants.FONT_OPEN_SANS_BOLD,
                                                     color=ui_constants.COLOUR_BKG_WHITE)

    screen.blit(txt_game_surface, (58, 75))
    screen.blit(txt_over_surface, (62, 105))

    _display_blinking_continue_message(game_state, screen)
    pygame.display.update()


def _display_blinking_continue_message(game_state: GameState, screen: pygame.Surface):
    """
    Displays the blinking continue message.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """
    if game_state.is_text_blinking:
        text_continue_surface = ui_constants.get_text_surface(ui_constants.TEXT_RETURN_TO_CONTINUE,
                                                              color=ui_constants.COLOUR_BKG_WHITE)
        screen.blit(text_continue_surface, (32, 195))
        game_state.is_text_blinking = False

    else:
        game_state.is_text_blinking = True
