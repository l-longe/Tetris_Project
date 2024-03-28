# game_play_mgr.py
""" This module contains the game play loop. """

from random import randint
import pygame
import pygame.locals as py_locals
import game_window
import tetrimino_check
from gamestate import GameState


def game_play_loop(game_state: GameState):
    """ The main game loop. """
    for event in pygame.event.get():

        if event.type == py_locals.QUIT:
            game_state.is_quit_triggered = True

        elif event.type == py_locals.USEREVENT:
            _draw_minos(game_state)

        elif event.type == py_locals.KEYDOWN:
            _process_user_input(game_state, event)

        pygame.display.update()


def _draw_minos(game_state: GameState):
    """
    Draws the minos on the screen.
    Steps:
    1. Draw the current mino and it's ghost
    2. Render the grid
    3. Erase the current minos, and it's ghost
    4. Increase pos_y by 1, if mino is not at the bottom

    :param game_state: Current game state and variables
    """
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)
    game_window.erase_current_mino_and_ghost(game_state)

    # Move mino down if it is not at the bottom
    if not tetrimino_check.is_at_bottom(game_state.pos_x, game_state.pos_y, game_state.mino, game_state.rotation):
        game_state.pos_y += 1
    else:  # The mino has landed, and we need to create a new mino
        _create_next_mino(game_state)


def _create_next_mino(game_state: GameState):
    """
    Creates a new mino at the default position of (x=3, y=0).

    :param game_state: Contains all the variables that represent the state of the game
    """
    # draw the current mino and it's ghost
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)

    # set the current mino to the next mino, and set the next mino to a random value
    game_state.mino = game_state.next_mino
    game_state.next_mino = randint(1, 7)

    # set to default position and rotation, and mark is_holding_mino as False
    game_state.pos_x, game_state.pos_y = 3, 0
    game_state.rotation = 0
    game_state.is_holding_mino = False


def _process_user_input(game_state: GameState, event):
    """
    Converts user input into game actions. \n
    - K_LEFT: Left = Move left
    - K_RIGHT: Right = Move right

    :param game_state: Current game state and variables
    :param event: The event to process
    """
    game_window.erase_current_mino_and_ghost(game_state)

    if event.key == py_locals.K_LEFT:
        _process_move_left(game_state)

    elif event.key == py_locals.K_RIGHT:
        _process_move_right(game_state)


def _process_move_left(game_state):
    """
    Processes a left move.

    :param game_state: Current game state and variables
    """

    # Move left if not at left edge
    if not tetrimino_check.is_at_left_edge(game_state.pos_x, game_state.pos_y, game_state.mino, game_state.rotation):
        game_state.pos_x -= 1

    # Now draw the mino, ghost and sidebar
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)


def _process_move_right(game_state: GameState):
    """
    Processes a right move.

    :param game_state: Current game state and variables
    """

    # Move right if not at right edge
    if not tetrimino_check.is_at_right_edge(game_state.pos_x, game_state.pos_y, game_state.mino, game_state.rotation):
        game_state.pos_x += 1

    # Now draw the mino, ghost and sidebar
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)