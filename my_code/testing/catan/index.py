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
MARGIN = 10
WIDTH, HEIGHT = COUNT_BLOCK * 4 + MARGIN * 5

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


while is_sero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


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
