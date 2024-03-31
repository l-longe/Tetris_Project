import pygame
import pygame.locals as py_locals

FRAME_RATE = 30
""" The frame rate of the game. """


def to_normal():
    """ Sets the speed of the game to the normal speed. """
    pygame.time.set_timer(pygame.USEREVENT, FRAME_RATE * 10)


def to_fastest():
    """ Sets the speed of the game to the fastest speed. """
    pygame.time.set_timer(pygame.USEREVENT, 1)


def to_dynamic():
    """
    Sets the speed of the game based on whether a key was recently pressed.
    """
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[py_locals.K_DOWN]:
        to_fastest()
    else:
        to_normal()
