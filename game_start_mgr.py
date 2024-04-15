# game_start_mgr.py
""" Start screen manager,
 which Manages the behaviour of the game before and while it is started. """

import pygame
from pygame.locals import Rect
import ui_constants
from screen_constants import SCREEN_HEIGHT, SCREEN_WIDTH


def update_loop(screen: pygame.Surface, clock: pygame.time.Clock):
    """
    Displays the start screen and processes user inputs.

    :param screen: The screen to draw on
    :param clock: The clock to control the frame rate
    """
    _draw_two_tone_background(screen)
    _display_title(screen)

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


def _display_title(screen: pygame.Surface):
    """
    Renders the title and the footer text.

    :param screen: The screen to draw on
    """

    title_text = ui_constants.get_text_surface(ui_constants.TEXT_TITLE, font_size=50)
    screen.blit(title_text, (75, 120))
