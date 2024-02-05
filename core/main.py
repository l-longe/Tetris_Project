import pygame
from pygame.locals import Rect
from screen_constants import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT, BLOCK_SIZE, SCREEN_SIZE

FRAME_RATE = 30

TEXT_TITLE = "TETRIS"
""" The title of the game. """

# Background colors
COLOUR_BKG_BLACK = (10, 10, 10)
COLOUR_BKG_WHITE = (255, 255, 255)
COLOUR_BKG_GREY_1 = (26, 26, 26)
COLOUR_BKG_GREY_2 = (35, 35, 35)
COLOUR_BKG_GREY_3 = (55, 55, 55)
COLOUR_BKG_BEIGE = (255, 255, 204)
COLOUR_BKG_BROWN = (153, 102, 51)


def draw_grid():
    for x in range(BOARD_COLUMN_COUNT):
        for y in range(BOARD_ROW_COUNT):
            pos_x = BLOCK_SIZE + (BLOCK_SIZE * x)  # add 1 to x to account for the border
            pos_y = BLOCK_SIZE + (BLOCK_SIZE * y)  # add 1 to y to account for the border
            _draw_grid_cell(pos_x, pos_y, COLOUR_BKG_GREY_3)


def _draw_grid_cell(pos_x, pos_y, color):
    """
    Draw a cell at the given position with the given color.

    :param pos_x: The x position of the cell
    :param pos_y: The y position of the cell
    :param color: The color of the cell
    """

    # Draw the cell
    pygame.draw.rect(
        screen,
        color,
        Rect(pos_x, pos_y, BLOCK_SIZE, BLOCK_SIZE)
    )

    # Draw the border of the cell
    pygame.draw.rect(
        screen,
        COLOUR_BKG_GREY_1,
        Rect(pos_x, pos_y, BLOCK_SIZE, BLOCK_SIZE),
        1
    )


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.time.set_timer(pygame.USEREVENT, FRAME_RATE * 10)
    pygame.display.set_caption(TEXT_TITLE)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(COLOUR_BKG_GREY_1)
        draw_grid()
        pygame.display.update()

    pygame.quit()
