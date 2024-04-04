from logics import *
import pygame
import sys


# 17. Переносим всю отрисовку интерфейса в функцию
def draw_interface():
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    # 14. создаем шрифт для отображения цифр на нашем игровом поле - название и размер
    font = pygame.font.SysFont('Comic Sans MS', 70)
    # 15. Передвинули вывод массива в консоль перед отрисовкой игры, чтобы не было опоздания
    pretty_print(mas)
    # 13. рисуем квадраты игрового поля
    for row in range(BLOCK):
        for column in range(BLOCK):
            # 14.1 находим значение ,которое хранится в массиве
            value = mas[row][column]
            # 14.2 прописываем, что будем писать и как
            text = font.render(f'{value}', True, BLACK )  # значение, обтекание шрифта и цвет
            w = column * SIZE_BLOCK + (column+1) * MARGIN
            h = (row * SIZE_BLOCK + (row+1) * MARGIN) + 110
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))  # 16.1 меняем цвет ячейки
            # в соответствии со значением из словаря COLORS
            # 14.3 условие для вывода значения на квадрате
            if value != 0:
                font_w, font_h = text.get_size()  # 14.4 узнаем размер текста
                text_x = w + (SIZE_BLOCK - font_w) / 2  # 14.5 координата размещение текста в квадрате по Х
                text_y = h + (SIZE_BLOCK - font_h) / 2  # 14.6 координата размещение текста в квадрате по У
                screen.blit(text, (text_x, text_y))  # 14.7 размещаем текст на экране по координатам


# 1. создаем двухмерный массив. он проиндексирован. у каждого эл. 2 индекса
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# 16. создаем словарь для того ,чтобы раскрасить наши ячейки по значению в массиве
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 128, 0),
    32: (255, 0, 128),
    64: (128, 0, 0),
    128: (255, 0, 0),
    256: (128, 128, 255),
    512: (155, 128, 128),
    1024: (0, 128, 255),
    2048: (0, 128, 0),
}

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

draw_interface()  # 17.2 вставляем функцию отрисовки интерфейса
pygame.display.update()  # 17.3 обновляем экран перед циклом, сразу игра будет видна

# 8. Создаем цикл игры
while is_zero_in_mas(mas):
    for event in pygame.event.get():  # 12.1 обработка события - закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # 12.2 обработка события - нажатие на любую клавишу
            # 19. подключаем функцию обработки события при нажатии кнопки влево на клавиатуре
            if event.key == pygame.K_LEFT:
                mas = move_left(mas)
            # 21. подключаем функцию обработки события при нажатии кнопки вправо на клавиатуре
            if event.key == pygame.K_RIGHT:
                mas = move_right(mas)
            # 23. подключаем функцию обработки события при нажатии кнопки вверх на клавиатуре
            if event.key == pygame.K_UP:
                mas = move_up(mas)
            # 25. подключаем функцию обработки события при нажатии кнопки вниз на клавиатуре
            if event.key == pygame.K_DOWN:
                mas = move_down(mas)
            # 12.3 переносим данные цикла в это условие
            # input()
            empty = get_empty_list(mas)  # 8.1 переменная, которая принимает список пустых ячеек
            random.shuffle(empty)  # 8.2 перемешивает элементы массива
            random_num = empty.pop()  # 8.3 удаляет последний элемент списка и возвращает его в переменную num
            x, y = get_index_from_number(random_num)  # 8.4 получаем координаты нашего числа
            mas = insert_2_or_4(mas, x, y)  # 8.5 присваиваем по этим координатам 2 или 4 в ячейку
            print(f'Заполнен элемент под номером: {random_num}. Координаты: {x}, {y}')

            draw_interface()  # 17.1 вставляем функцию отрисовки интерфейса после добавления нового элемента
            pygame.display.update()  # подвинули внутрь цикла, чтобы обновление только при нажатии клавиши сразу

# ----------------------------- COMMENTS ----------------------------
# массив можно писать в таком виде: mas_2 = [[0]*4 for i in range(4)]
