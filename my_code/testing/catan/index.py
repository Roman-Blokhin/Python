import random
import sys
import pygame

pygame.init()


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_num_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_num(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_num_from_index(i, j)
                empty.append(num)
    return empty


def insert_num_to_mas(mas, x, y):
    if random.random() <= 0.2:
        mas[x][y] = 1
    elif random.random() <= 0.4:
        mas[x][y] = 2
    elif random.random() <= 0.5:
        mas[x][y] = 3
    elif random.random() <= 0.8:
        mas[x][y] = 4
    elif random.random() <= 1:
        mas[x][y] = 5
    return mas


def insert():
    pass


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


while True:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit(0)

    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_number = empty.pop()
    x, y = get_index_from_num(random_number)
    print(f'Выбрано число: {random_number}, с координатами: x = {x}, y = {y}')
    mas = insert_num_to_mas(mas, x, y)
    print(get_empty_list(mas))
    pretty_print(mas)

    # pygame.display.update()

# 16 = 3 red 5 green 4 sheep 2 grey 2 yellow
