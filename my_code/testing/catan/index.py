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

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catan')


while is_sero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    for row in range(COUNT_BLOCK):
        for column in range(COUNT_BLOCK):
            x = column * SIZE_BLOCK + MARGIN * (column + 1)
            y = row * SIZE_BLOCK + MARGIN * (row + 1) + 110
            pygame.draw.rect(screen, GRAY, (x, y, SIZE_BLOCK, SIZE_BLOCK))

    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_number = empty.pop()
    x, y = get_index_from_num(random_number)
    print(f'Выбрано число: {random_number}, с координатами: x = {x}, y = {y}')
    mas = insert_num_to_mas(mas, x, y)
    print(get_empty_list(mas))
    pretty_print(mas)

    pygame.display.update()

# 16 = 3 red 5 green 4 sheep 2 grey 2 yellow
