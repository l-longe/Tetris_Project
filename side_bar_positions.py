# side_bar_positions.py
""" Contains the positions of the sidebar elements. """

from screen_constants import BLOCK_SIZE


class Side_Bar_Positions:
    """ The positions of the sidebar elements. """

    all_mino_pos_x = BLOCK_SIZE * 13  # BLOCK_SIZE * 10 + BLOCK_SIZE * 2 + BLOCK_SIZE
    """ The x position of the first mino in the sidebar,
     regardless of the mino's shape, 
     or whether it is the next or hold mino.
     """

    hold_mino_pos_y = 50
    """ The y position of the hold mino in the sidebar. """

    next_mino_pos_y = 140
    """ The y position of the next mino in the sidebar. """
