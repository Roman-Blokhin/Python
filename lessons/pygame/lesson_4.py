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

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Me program')
clock = pygame.time.Clock()

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(FPS)
    screen.fill(FRAME_COLOR)

    # 3. цикл для обработки квадратов по горизонтали
    for column in range(count_blocks):
        # 4. цикл для обработки квадратов по вертикалиД
        for row in range(count_blocks):
            x = column * width + margin * (column + 1)
            y = row * height + margin * (row + 1)
            # 2. рисуем квадрат на экране
            pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()
