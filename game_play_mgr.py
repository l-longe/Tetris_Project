# game_play_mgr.py
""" This module contains the game play loop. """

from random import randint
import pygame
import pygame.locals as py_locals
import game_window
import tetrimino_check
from gamestate import GameState
import game_speed


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
    game_speed.to_dynamic(game_state)

    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)
    game_window.erase_current_mino_and_ghost(game_state)

    # Move mino down if it is not at the bottom
    if not tetrimino_check.is_at_bottom(game_state.pos_x, game_state.pos_y, game_state.mino, game_state.rotation):
        game_state.pos_y += 1
    else:  # The mino has landed, and we need to create a new mino
        _create_next_mino(game_state)

    _remove_full_rows(game_state)

    # Increase level, goal and game speed (complexity) if goal is reached
    if game_state.goal < 1 and game_state.level < 15:
        game_state.level += 1
        game_state.goal += game_state.level * 5
        game_state.frame_rate = int(game_state.frame_rate * 0.8)


def _create_next_mino(game_state: GameState):
    """
    Creates a new mino at the default position of (x=3, y=0).

    :param game_state: Contains all the variables that represent the state of the game
    """
    # Give the user a short delay to move the mino left or right, just after it (softly) lands
    if not game_state.in_hard_drop and game_state.post_landing_delay < 6:
        game_state.post_landing_delay += 1
    else:
        # Reset the hard drop and after drop delay variables
        game_state.in_hard_drop = False
        game_state.post_landing_delay = 0
        game_state.score += 10 * game_state.level  # Add 10 points (per level) for each landed mino

        # draw the current mino and it's ghost
        game_window.draw_current_mino_and_ghost(game_state)
        game_window.render(game_state)

        if tetrimino_check.can_fit_in_grid(game_state.next_mino):
            # set the current mino to the next mino, and set the next mino to a random value
            game_state.mino = game_state.next_mino
            game_state.next_mino = randint(1, 7)

            # set to default position and rotation, and mark is_holding_mino as False
            game_state.pos_x, game_state.pos_y = 3, 0
            game_state.rotation = 0
            game_state.is_holding_mino = False
        else:
            # set game over if next mino cannot fit in grid
            game_state.is_game_over = True
            pygame.time.set_timer(pygame.USEREVENT, 1)


def _remove_full_rows(game_state: GameState):
    """
    Removes full rows (if any). \n
    Full rows are rows that are completely filled with blocks.

    :param game_state: Current game state and variables
    """
    removed_rows = 0
    for j in range(21):
        is_full = True
        for i in range(10):
            if game_state.grid[i][j] == 0:
                is_full = False
        if is_full:
            removed_rows += 1
            k = j
            while k > 0:
                for i in range(10):
                    game_state.grid[i][k] = game_state.grid[i][k - 1]
                k -= 1
    if removed_rows == 1:
        game_state.score += 50 * game_state.level

    elif removed_rows == 2:
        game_state.score += 150 * game_state.level

    elif removed_rows == 3:
        game_state.score += 350 * game_state.level

    elif removed_rows == 4:
        game_state.score += 1000 * game_state.level

    game_state.goal -= removed_rows


def _process_user_input(game_state: GameState, event):
    """
    Converts user input into game actions. \n
    - K_LEFT: Left = Move left
    - K_RIGHT: Right = Move right
    - K_UP or K_w: Up or x = Rotate right
    - K_DOWN or K_s: z or Left ctrl = Rotate left
    - K_SPACE: Space = Hard drop
    - K_LSHIFT or K_z: Left shift or z = Hold

    :param game_state: Current game state and variables
    :param event: The event to process
    """
    game_window.erase_current_mino_and_ghost(game_state)

    if event.key == py_locals.K_LEFT or event.key == py_locals.K_a:
        _process_move_left(game_state)

    elif event.key == py_locals.K_RIGHT or event.key == py_locals.K_d:
        _process_move_right(game_state)

    elif event.key == py_locals.K_UP or event.key == py_locals.K_w:
        _process_rotate_right(game_state)

    elif event.key == py_locals.K_DOWN or event.key == py_locals.K_s:
        _process_rotate_left(game_state)

    elif event.key == py_locals.K_SPACE:
        _process_hard_drop(game_state)

    elif event.key == py_locals.K_LSHIFT or event.key == py_locals.K_z:
        _process_hold(game_state)


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


def _process_rotate_right(game_state: GameState):
    """
    Rotates the current mino to the right.

    It also performs a kick if the mino cannot rotate at the current position.\n
    A kick is when the mino is moved to the left or right, or up or down, to allow it to rotate.

    A series of kicks are attempted in the following order:
    1. Kick down
    2. Kick left
    3. Kick right
    4. Kick up
    5. Kick down and left
    6. Kick down and right

    :param game_state: Current game state and variables
    """

    # Creating a copy of the game state variable so that subsequent lines of code are not too long
    state = game_state  # state is a reference to game_state. changes to state will change game_state

    # Rotate right
    if tetrimino_check.can_rotate_right(state.pos_x, state.pos_y, state.mino, state.rotation):
        state.rotation += 1

    # Kick down
    elif tetrimino_check.can_rotate_right(state.pos_x, state.pos_y - 1, state.mino, state.rotation):
        state.pos_y -= 1
        state.rotation += 1

    # Kick left
    elif tetrimino_check.can_rotate_right(state.pos_x + 1, state.pos_y, state.mino, state.rotation):
        state.pos_x += 1
        state.rotation += 1

    # Kick right
    elif tetrimino_check.can_rotate_right(state.pos_x - 1, state.pos_y, state.mino, state.rotation):
        state.pos_x -= 1
        state.rotation += 1

    # Kick up
    elif tetrimino_check.can_rotate_right(state.pos_x, state.pos_y - 2, state.mino, state.rotation):
        state.pos_y -= 2
        state.rotation += 1

    # Kick down and left
    elif tetrimino_check.can_rotate_right(state.pos_x + 2, state.pos_y, state.mino, state.rotation):
        state.pos_x += 2
        state.rotation += 1

    # Kick down and right
    elif tetrimino_check.can_rotate_right(state.pos_x - 2, state.pos_y, state.mino, state.rotation):
        state.pos_x -= 2
        state.rotation += 1

    # Rotate back to 0 if rotation is 4
    if game_state.rotation == 4:
        game_state.rotation = 0

    # Noe draw the mino, ghost and sidebar
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)


def _process_rotate_left(game_state: GameState):
    """
    Rotates the current mino to the left.

    It also performs a kick if the mino cannot rotate at the current position.\n
    A kick is when the mino is moved to the left or right, or up or down, to allow it to rotate.

    A series of kicks are attempted in the following order:
    1. Kick down
    2. Kick left
    3. Kick right
    4. Kick up
    5. Kick down and left
    6. Kick down and right

    :param game_state: Current game state and variables
    """

    # Creating a copy of the game state variable so that subsequent lines of code are not too long
    state = game_state  # state is a reference to game_state. changes to state will change game_state

    # Rotate left
    if tetrimino_check.can_rotate_left(state.pos_x, state.pos_y, state.mino, state.rotation):
        state.rotation -= 1

    # Kick down
    elif tetrimino_check.can_rotate_left(state.pos_x, state.pos_y - 1, state.mino, state.rotation):
        state.pos_y -= 1
        state.rotation -= 1

    # Kick left
    elif tetrimino_check.can_rotate_left(state.pos_x + 1, state.pos_y, state.mino, state.rotation):
        state.pos_x += 1
        state.rotation -= 1

    # Kick right
    elif tetrimino_check.can_rotate_left(state.pos_x - 1, state.pos_y, state.mino, state.rotation):
        state.pos_x -= 1
        state.rotation -= 1

    # Kick up
    elif tetrimino_check.can_rotate_left(state.pos_x, state.pos_y - 2, state.mino, state.rotation):
        state.pos_y -= 2
        state.rotation += 1

    # Kick down and left
    elif tetrimino_check.can_rotate_left(state.pos_x + 2, state.pos_y, state.mino, state.rotation):
        state.pos_x += 2
        state.rotation += 1

    # Kick down and right
    elif tetrimino_check.can_rotate_left(state.pos_x - 2, state.pos_y, state.mino, state.rotation):
        state.pos_x -= 2

    # Rotate back to 3 if rotation is -1
    if game_state.rotation == -1:
        game_state.rotation = 3

    # Now draw the mino, ghost and sidebar
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)


def _process_hard_drop(game_state: GameState):
    """
    Processes a hard drop. \n
    A hard drop is when the mino is dropped to the bottom instantly.

    :param game_state: Current game state and variables
    """

    while not tetrimino_check.is_at_bottom(game_state.pos_x, game_state.pos_y, game_state.mino, game_state.rotation):
        game_state.pos_y += 1

    game_state.in_hard_drop = True
    game_speed.to_fastest()

    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)


def _process_hold(game_state: GameState):
    """
    Processes the hold user input. \n
    Hold is when the current mino is swapped with the mino on hold.

    :param game_state: Current game state and variables
    """

    if not game_state.is_holding_mino:

        # If no mino is currently on hold,
        # set hold mino to current mino and generate a new mino
        if game_state.held_mino == -1:
            game_state.held_mino = game_state.mino
            game_state.mino = game_state.next_mino
            game_state.next_mino = randint(1, 7)

        else:
            # Otherwise, swap hold mino with current mino
            game_state.held_mino, game_state.mino = game_state.mino, game_state.held_mino

        # Put the new or swapped mino at the default position and rotation,
        # and mark is_holding_mino as True
        game_state.pos_x, game_state.pos_y = 3, 0
        game_state.rotation = 0
        game_state.is_holding_mino = True

    # Now draw the mino, ghost and sidebar
    game_window.draw_current_mino_and_ghost(game_state)
    game_window.render(game_state)
