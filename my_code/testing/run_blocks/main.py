# ХОЧУ СДЕЛАТЬ ПЕРВЫЙ МАКЕТ ДЛЯ ИГРЫ SPACE BATTLE, ГДЕ КОРАБЛИ ПРОТИВНИКА ЛЕТЯТ НА ТЕБЯ, А ТЕБЕ НУЖНО ИХ СБИВАТЬ

import pygame
pygame.init()

# ---------------------- variables ------------------------

FRAME_COLOR = (100, 100, 100)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (400, 600)

# ---------------------- window ------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Running bloks')
img = pygame.image.load('space_logo.png')
pygame.display.set_icon(img)

# ---------------------- cycle ------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

