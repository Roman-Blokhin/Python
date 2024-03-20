import random


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


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(get_empty_list(mas))
print(get_index_from_num(1))
pretty_print(mas)

# 16 = 3 red 5 green 4 sheep 2 grey 2 yellow