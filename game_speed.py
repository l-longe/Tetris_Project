import pygame
import pygame.locals as py_locals
from gamestate import GameState


def to_normal(game_state: GameState):
    """ Sets the speed of the game to the normal speed. """
    pygame.time.set_timer(pygame.USEREVENT, game_state.frame_rate * 10)


def to_fastest():
    """ Sets the speed of the game to the fastest speed. """
    pygame.time.set_timer(pygame.USEREVENT, 1)


def to_dynamic(game_state: GameState):
    """
    Sets the speed of the game based on whether a key was recently pressed.
    """
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[py_locals.K_DOWN]:
        to_fastest()
    else:
        to_normal(game_state)
