# Как создать игровое поле для своей игры

import pygame

pygame.init()

# ------------------------------------------ VARIABLES ------------------------------------------

FRAME_COLOR = (100, 100, 100)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (510, 510)
width = height = 40  # размер квадратика
x = 0
y = 0
count_blocks = 10
margin = 10

FPS = 60

# 8. создаем двухмерный массив для определения квадрата, на который мы кликнули
mas = [[0] * 10 for i in range(10)]

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Me program')
clock = pygame.time.Clock()

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # 5. обрабатываем нажатие клавиши мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 6. если тип - нажатие клавиши
            x_mouse, y_mouse = pygame.mouse.get_pos()  # 7. присваиваем нажатию считывание координат
            print(f'x = {x_mouse}, y = {y_mouse}')
            # 9. вычисляем колонку и ряд, на который кликнули
            column = x_mouse // (width + margin)
            row = y_mouse // (height + margin)
            mas[row][column] ^= 1  # 10. клик на квадрат, то значение = 1, если кликнули еще раз, значение возвращается

    clock.tick(FPS)
    screen.fill(FRAME_COLOR)

    # 4. цикл для обработки квадратов по вертикалиД
    for row in range(count_blocks):
        # 3. цикл для обработки квадратов по горизонтали
        for column in range(count_blocks):
            # 11. устанавливаем цвет для нажатого квадрата
            if mas[row][column] == 1:
                color = RED
            else:
                color = WHITE

            x = column * width + margin * (column + 1)
            y = row * height + margin * (row + 1)
            # 2. рисуем квадрат на экране
            pygame.draw.rect(screen, color, (x, y, width, height))

    pygame.display.update()
