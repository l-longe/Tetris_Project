# side_bar_positions.py
""" Contains the positions of the sidebar elements. """

import ui_constants
from screen_constants import BLOCK_SIZE


class Side_Bar_Positions:
    """ The positions of the sidebar elements. """

    all_mino_pos_x = BLOCK_SIZE * 13  # BLOCK_SIZE * 10 + BLOCK_SIZE * 2 + BLOCK_SIZE
    """ The x position of the first mino in the sidebar,
     regardless of the mino's shape, 
     or whether it is the next or hold mino.
     """

    all_text_pos_x = all_mino_pos_x - 10
    """ The x position of the texts in the sidebar. """

    hold_mino_pos_y = 50
    """ The y position of the hold mino in the sidebar. """

    next_mino_pos_y = 140
    """ The y position of the next mino in the sidebar. """

    hold_text_pos_y = 14
    """ The y position of the hold text in the sidebar. """

    next_text_pos_y = 104
    """ The y position of the next text in the sidebar. """

    hold_text = ui_constants.get_text_surface("HOLD")
    """ The hold label in the sidebar. """

    next_text = ui_constants.get_text_surface("NEXT")
    """ The next label in the sidebar. """
