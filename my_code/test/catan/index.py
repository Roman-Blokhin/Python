import random


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_num_from_index(i, j):
    return i * 4 + j + 1


def get_empty_list(mas):
    empty = []
    for i in range(5):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_num_from_index(i, j)
                empty.append(num)
    return empty


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(get_empty_list(mas))
pretty_print(mas)
