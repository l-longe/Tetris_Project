# game_start_mgr.py
""" Start screen manager,
 which Manages the behaviour of the game before and while it is started. """

import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, Rect
import ui_constants
from gamestate import GameState
from screen_constants import SCREEN_HEIGHT, SCREEN_WIDTH


def update_loop(game_state: GameState, screen: pygame.Surface, clock: pygame.time.Clock):
    """
    Displays the start screen and leaderboard, and processes user inputs.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    :param clock: The clock to control the frame rate
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state.is_quit_triggered = True

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                game_state.is_game_started = True

    _draw_two_tone_background(screen)
    _display_title_and_footer(screen)
    _display_blinking_start_message(game_state, screen)

    if not game_state.is_game_started:
        pygame.display.update()
        clock.tick(3)


def _draw_two_tone_background(screen: pygame.Surface):
    """
    Draws the White and Grey backgrounds over the default black background.

    :param screen: The screen to draw on
    """
    # Draw beige top-half background
    screen.fill(ui_constants.COLOUR_BKG_BEIGE)

    # Draw brown bottom-half background
    pygame.draw.rect(
        screen,
        ui_constants.COLOUR_BKG_BROWN,
        Rect(0, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT/2)
    )


def _display_title_and_footer(screen: pygame.Surface):
    """
    Renders the title and the footer text.

    :param screen: The screen to draw on
    """

    # Render the main title text
    main_title_text = ui_constants.get_text_surface(ui_constants.GAME_TITLE, font_size=50)
    screen.blit(main_title_text, (75, 120))

    # Render the footer text
    footer_text = ui_constants.get_text_surface(ui_constants.PROJECT_TITLE, font_size=10)
    screen.blit(footer_text, (35, 355))

def _display_blinking_start_message(game_state: GameState, screen: pygame.Surface):
    """
    Renders the blinking start message.

    :param game_state: Current game state and variables
    :param screen: The screen to draw on
    """

    if game_state.is_text_blinking:
        start_msg = ui_constants.get_text_surface(ui_constants.START_MESSAGE,
                                                  color=ui_constants.COLOUR_BKG_WHITE)
        screen.blit(start_msg, (92, 195))
        game_state.is_text_blinking = False
    else:
        game_state.is_text_blinking = True
