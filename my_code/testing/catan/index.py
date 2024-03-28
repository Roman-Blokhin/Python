import pygame
import sys
from logic import *
pygame.init()


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (155, 155, 155)

COUNT_BLOCK = 4
SIZE_BLOCK = 100
MARGIN = 10
WIDTH = SIZE_BLOCK * COUNT_BLOCK + MARGIN * (COUNT_BLOCK + 1)
HEIGHT = WIDTH + 110
TITLE_RECT = pygame.Rect(0, 0, WIDTH, 110)

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


COLORS = {
    0: (70, 130, 180),
    1: (0, 100, 0),
    2: (240, 128, 128),
    3: (0, 250, 154),
    4: (255, 255, 128),
    5: (169, 169, 169),
}


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catan')

pretty_print(mas)
pygame.display.update()

while is_sero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, WHITE, (TITLE_RECT))
            font = pygame.font.SysFont('Comic Sans MS', 70)
            pretty_print(mas)

            for row in range(COUNT_BLOCK):
                for column in range(COUNT_BLOCK):
                    value = mas[row][column]
                    text = font.render(f'{value}', True, BLACK)
                    x = column * SIZE_BLOCK + MARGIN * (column + 1)
                    y = row * SIZE_BLOCK + MARGIN * (row + 1) + 110
                    pygame.draw.rect(screen, COLORS[value], (x, y, SIZE_BLOCK, SIZE_BLOCK))

                    if value != 0:
                        font_w, font_h = text.get_size()
                        text_x = x + (SIZE_BLOCK - font_w) / 2
                        text_y = y + (SIZE_BLOCK - font_h) / 2

            # input()
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_number = empty.pop()
            x, y = get_index_from_num(random_number)
            print(f'Выбрано число: {random_number}, с координатами: x = {x}, y = {y}')
            mas = insert_num_to_mas(mas, x, y)
            print(get_empty_list(mas))


            pygame.display.update()

# 16 = 3 red 5 green 4 sheep 2 grey 2 yellow
