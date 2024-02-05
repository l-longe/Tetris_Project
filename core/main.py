import pygame
import game_window
from screen_constants import SCREEN_SIZE
from ui_constants import COLOUR_BKG_GREY_1

FRAME_RATE = 30

TEXT_TITLE = "TETRIS"
""" The title of the game. """


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    _screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.time.set_timer(pygame.USEREVENT, FRAME_RATE * 10)
    pygame.display.set_caption(TEXT_TITLE)

    game_window.screen = _screen  # Save a reference to the screen in screen_renderer

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        _screen.fill(COLOUR_BKG_GREY_1)
        game_window.draw_grid()
        pygame.display.update()

    pygame.quit()
