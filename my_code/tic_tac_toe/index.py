# ИГРА КРЕСТИКИ-НОЛИКИ

import pygame

pygame.init()

# ------------------------------------------ VARIABLES ------------------------------------------

FRAME_COLOR = (100, 100, 100)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

count_block = 3
block_size = 100
margin = 15
width = height = block_size * 3 + margin * 4
size = (width, height)

# 2. создали массив для присваивания каждому квадрату значение - 0
mas = [[0]*3 for i in range(count_block)]

FPS = 60

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('КРЕСТИКИ-НОЛИКИ')
img = pygame.image.load('logo.png')
pygame.display.set_icon(img)
clock = pygame.time.Clock()

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # 3. обрабатываем нажатие левой кнопки мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 4. получение координат нажатия на экране игры
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(x_mouse, y_mouse)


    clock.tick(FPS)
    screen.fill(FRAME_COLOR)

    # 1. прописали цикл вывода квадратов игрового поля
    for row in range(count_block):
        for col in range(count_block):

            x = col * block_size + margin * (col + 1)
            y = row * block_size + margin * (row + 1)
            pygame.draw.rect(screen, RED, (x, y, block_size, block_size))

    pygame.display.update()
