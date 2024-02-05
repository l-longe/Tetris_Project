import pygame
import game_window
from screen_constants import SCREEN_SIZE

FRAME_RATE = 30

TEXT_TITLE = "TETRIS"
""" The title of the game. """


def _update_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game_window.render()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    _screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.time.set_timer(pygame.USEREVENT, FRAME_RATE * 10)
    pygame.display.set_caption(TEXT_TITLE)

    game_window.screen = _screen  # Save a reference to the screen in screen_renderer

    _update_loop()
