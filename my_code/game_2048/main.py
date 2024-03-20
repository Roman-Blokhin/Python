from logics import *
import pygame

# 1. создаем двухмерный массив. он проиндексирован. у каждого эл. 2 индекса
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


# 10. прописываем константы и переменные
BLOCK = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCK * SIZE_BLOCK + MARGIN * (BLOCK + 1)
HEIGHT = WIDTH + 110


# 2. мы можем положить определенные числа в наши ячейки. берем индекс эл. по Х и У

mas[1][2] = 2
mas[3][0] = 2

print(get_empty_list(mas))
pretty_print(mas)

# 8. Создаем цикл игры
while is_zero_in_mas(mas):
    input()
    empty = get_empty_list(mas)  # 8.1 переменная, которая принимает список пустых ячеек
    random.shuffle(empty)  # 8.2 перемешивает элементы массива
    random_num = empty.pop()  # 8.3 удаляет последний элемент списка и возвращает его в переменную num
    x, y = get_index_from_number(random_num)  # 8.4 получаем координаты нашего числа
    mas = insert_2_or_4(mas, x, y)  # 8.5 присваиваем по этим координатам 2 или 4 в ячейку
    print(f'Заполнен элемент под номером: {random_num}. Координаты: {x}, {y}')
    pretty_print(mas)


# ----------------------------- COMMENTS ----------------------------
# массив можно писать в таком виде: mas_2 = [[0]*4 for i in range(4)]
