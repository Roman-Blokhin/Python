import pygame

pygame.init()

# ------------------------------------------ VARIABLES ------------------------------------------

FRAME_COLOR = (100, 100, 100)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

block_size = 100
margin = 15
width = height = block_size * 3 + margin * 4
size = (width, height)

FPS = 60

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Крестики нолики')
img = pygame.image.load('logo.png')
pygame.display.set_icon(img)
clock = pygame.time.Clock()

# 2. массив для прикрепления значений к клеткам
mas = [[0] * 3 for i in range(3)]

qwerty = 0  # 6. переменная, которая будет увеличиваться на один, это поможет чередовать цвета

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # 3. обработка кликов мышки и получение координат
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (block_size + margin)
            row = y_mouse // (block_size + margin)
            print(x_mouse, y_mouse)
            # 4. присваиваем название нажатию
            if qwerty % 2 == 0:
                mas[row][column] = 'x'
            else:
                mas[row][column] = 'y'

            qwerty += 1

    clock.tick(FPS)
    screen.fill(FRAME_COLOR)

    # 1. отображаем игровое поле
    for row in range(3):
        for column in range(3):
            # 5. условие для первого нажатия по изменению цвета у квадрата
            if mas[row][column] == 'x':
                color = RED
            elif mas[row][column] == 'y':
                color = GREEN
            else:
                color = WHITE


            x = column * block_size + margin * (column + 1)
            y = row * block_size + margin * (row + 1)
            pygame.draw.rect(screen, color, (x, y, block_size, block_size))

    pygame.display.update()
