from logics import *
import pygame
import sys

# 1. создаем двухмерный массив. он проиндексирован. у каждого эл. 2 индекса
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# 10. прописываем константы и переменные
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)

BLOCK = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCK * SIZE_BLOCK + MARGIN * (BLOCK + 1)
HEIGHT = WIDTH + 110

# 11. пишем визуал на pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)  # 11.1 задаем координаты прямоугольника

# 2. мы можем положить определенные числа в наши ячейки. берем индекс эл. по Х и У

mas[1][2] = 2
mas[3][0] = 2

print(get_empty_list(mas))
pretty_print(mas)

# 8. Создаем цикл игры
while is_zero_in_mas(mas):
    for event in pygame.event.get():  # 12.1 обработка события - закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # 12.2 обработка события - нажатие на любую клавишу
            pygame.draw.rect(screen, WHITE, TITLE_REC)
            # 13. рисуем квадраты игрового поля
            for row in range(BLOCK):
                for column in range(BLOCK):
                    w = column * SIZE_BLOCK + (column+1) * MARGIN
                    h = (row * SIZE_BLOCK + (row+1) * MARGIN) + 110
                    pygame.draw.rect(screen, GRAY, (w, h, SIZE_BLOCK, SIZE_BLOCK))

            # 12.3 переносим данные цикла в это условие
            # input()
            empty = get_empty_list(mas)  # 8.1 переменная, которая принимает список пустых ячеек
            random.shuffle(empty)  # 8.2 перемешивает элементы массива
            random_num = empty.pop()  # 8.3 удаляет последний элемент списка и возвращает его в переменную num
            x, y = get_index_from_number(random_num)  # 8.4 получаем координаты нашего числа
            mas = insert_2_or_4(mas, x, y)  # 8.5 присваиваем по этим координатам 2 или 4 в ячейку
            print(f'Заполнен элемент под номером: {random_num}. Координаты: {x}, {y}')
            pretty_print(mas)

    pygame.display.update()

# ----------------------------- COMMENTS ----------------------------
# массив можно писать в таком виде: mas_2 = [[0]*4 for i in range(4)]
