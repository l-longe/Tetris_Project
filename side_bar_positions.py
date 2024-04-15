# side_bar_positions.py
""" Contains the positions of the sidebar elements. """

import pygame
import ui_constants
from screen_constants import BLOCK_SIZE


class Side_Bar_Positions:
    """ The positions of the sidebar elements. """

    all_mino_pos_x = BLOCK_SIZE * 13  # BLOCK_SIZE * 10 + BLOCK_SIZE * 2 + BLOCK_SIZE
    """ The x position of the first mino in the sidebar,
     regardless of the mino's shape, 
     or whether it is the next or hold mino.
     """

    all_label_pos_x = all_mino_pos_x - 10
    """ The x position of the texts in the sidebar. """

    all_numbers_pos_x = all_mino_pos_x
    """ The x position of the numbers in the sidebar. """

    hold_label_pos_y = 14
    """ The y position of the hold text in the sidebar. """

    hold_mino_pos_y = 50
    """ The y position of the hold mino in the sidebar. """

    next_label_pos_y = 104
    """ The y position of the next text in the sidebar. """

    next_mino_pos_y = 140
    """ The y position of the next mino in the sidebar. """

    score_label_pos_y = 194
    """ The y position of the score text in the sidebar. """

    score_number_pos_y = 210
    """ The y position of the score number in the sidebar. """

    level_label_pos_y = 254
    """ The y position of the level text in the sidebar. """

    level_number_pos_y = 270
    """ The y position of the level number in the sidebar. """

    goal_label_pos_y = 314
    """ The y position of the goal text in the sidebar. """

    goal_number_pos_y = 330
    """ The y position of the goal number in the sidebar. """

    hold_label = ui_constants.get_text_surface("HOLD")
    """ The hold label in the sidebar. """

    next_label = ui_constants.get_text_surface("NEXT")
    """ The next label in the sidebar. """

    score_label = ui_constants.get_text_surface("SCORE")
    """ The score label in the sidebar. """

    level_label = ui_constants.get_text_surface("LEVEL")
    """ The level label in the sidebar. """

    goal_label = ui_constants.get_text_surface("GOAL")
    """ The goal label in the sidebar. """

    def __init__(self):
        pass

    @staticmethod
    def get_value_text_surface(value: str) -> pygame.Surface:
        """
        Returns a surface containing the value of the given text.

        :param value: The value to render
        :return: The rendered value
        """
        return ui_constants.get_text_surface(value, font_size=20)
