# main.py

import pygame
import game_window
from screen_constants import SCREEN_SIZE
import tetriminos

FRAME_RATE = 30

TEXT_TITLE = "TETRIS"
""" The title of the game. """


def _update_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                # game_window.draw_mino(tetriminos.I_rotation_1, 3, 0)
                # game_window.draw_mino(tetriminos.J_rotation_1, 3, 3)
                # game_window.draw_mino(tetriminos.L_rotation_1, 3, 6)
                # game_window.draw_mino(tetriminos.O_rotation_1, 3, 9)
                # game_window.draw_mino(tetriminos.S_rotation_1, 3, 12)
                # game_window.draw_mino(tetriminos.T_rotation_1, 3, 15)
                # game_window.draw_mino(tetriminos.Z_rotation_1, 3, 18)

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
    game_window.initialise_grid_cell_colours()

    _update_loop()
