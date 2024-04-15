# ui_constants.py
""" This module contains hard-coded settings for the UI. """

import pygame

pygame.init()

# Fonts
FONT_OPEN_SANS_LIGHT = "./fonts/OpenSans-Light.ttf"
FONT_OPEN_SANS_BOLD = "./fonts/OpenSans-Bold.ttf"
FONT_INCONSOLATA = "./fonts/Inconsolata/Inconsolata.otf"

_FONT_OPEN_SANS_LIGHT_50 = pygame.font.Font(FONT_OPEN_SANS_LIGHT, 50)
FONT_OPEN_SANS_LIGHT_30 = pygame.font.Font(FONT_OPEN_SANS_LIGHT, 30)
FONT_OPEN_SANS_LIGHT_20 = pygame.font.Font(FONT_OPEN_SANS_LIGHT, 20)
FONT_OPEN_SANS_LIGHT_13 = pygame.font.Font(FONT_OPEN_SANS_LIGHT, 13)
FONT_OPEN_SANS_LIGHT_10 = pygame.font.Font(FONT_OPEN_SANS_LIGHT, 10)

FONT_OPEN_SANS_BOLD_50 = pygame.font.Font(FONT_OPEN_SANS_BOLD, 50)
FONT_OPEN_SANS_BOLD_30 = pygame.font.Font(FONT_OPEN_SANS_BOLD, 30)

FONT_INCONSOLATA_30 = pygame.font.Font(FONT_INCONSOLATA, 30)
FONT_INCONSOLATA_13 = pygame.font.Font(FONT_INCONSOLATA, 13)


# Background colors
COLOUR_BKG_BLACK = (10, 10, 10)
COLOUR_BKG_WHITE = (255, 255, 255)
COLOUR_BKG_GREY_1 = (26, 26, 26)
COLOUR_BKG_GREY_2 = (35, 35, 35)
COLOUR_BKG_GREY_3 = (55, 55, 55)
COLOUR_BKG_BEIGE = (255, 255, 204)
COLOUR_BKG_BROWN = (153, 102, 51)

# Block colors
_COLOUR_BLOCK_I_CYAN = (102, 153, 204)  # A lighter shade of blue for (I)
_COLOUR_BLOCK_J_PINK = (153, 51, 102)  # A muted pink for (J)
_COLOUR_BLOCK_L_LIGHT_GREEN = (204, 204, 0)  # A vibrant yellow-green for (L)
_COLOUR_BLOCK_O_ORANGE = (255, 153, 51)  # A bright orange for (O)
_COLOUR_BLOCK_S_TEAL = (0, 153, 153)  # A teal color for (S)
_COLOUR_BLOCK_T_MAGENTA = (204, 0, 102)  # A deep magenta for (T)
_COLOUR_BLOCK_DARK_Z_GREEN = (51, 102, 0)  # A dark green for (Z)

# Block colors
BLOCK_COLOURS = [COLOUR_BKG_GREY_2,
                 _COLOUR_BLOCK_I_CYAN, _COLOUR_BLOCK_J_PINK, _COLOUR_BLOCK_L_LIGHT_GREEN,
                 _COLOUR_BLOCK_O_ORANGE, _COLOUR_BLOCK_S_TEAL, _COLOUR_BLOCK_T_MAGENTA,
                 _COLOUR_BLOCK_DARK_Z_GREEN, COLOUR_BKG_GREY_3]
""" The colors of the blocks in the game. """

GAME_TITLE = "TETRIS"
""" The title of the game. """

PROJECT_TITLE = "282110 _ Lathan Longe - Computing Project - 2024"
""" The full title of my project. """


TEXT_PAUSE = "PAUSED"
""" The text that appears when the game is paused. """

TEXT_GAME_OVER = ["GAME", "OVER"]
""" A list containing the two words that make up the game over text. """


def get_text_surface(text: str,
                     font_size: int = 13,
                     font_file=FONT_OPEN_SANS_LIGHT,
                     color: tuple = COLOUR_BKG_BLACK) -> pygame.Surface:
    """
    Returns a text surface with the given string.

    :param text: The text to render (and scale)
    :param font_size: The size of the font to render
    :param font_file: The font file to use
    :param color: The color of the text
    :return: A text surface with the given string
    """
    actual_font_size = int(font_size)
    font = pygame.font.Font(font_file, actual_font_size)

    text_surface = font.render(text, 1, color)
    return text_surface
