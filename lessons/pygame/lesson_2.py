# Шрифты в Pygame. Добавляем текст в окно игры

import pygame
pygame.init()  # 0. всегда прописываем для шрифтов

RED = (150, 0, 0)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)

size = (500, 500)

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Second lesson')
img = pygame.image.load('logo.png')
pygame.display.set_icon(img)

# 1. устанавливаем шрифт
font = pygame.font.SysFont('Comic Sans MS', 36)
# 2. переменная с текстом для вывода на экран(текст, сглаживание(0-нет, 1-да), цвет шрифта, цвет фона)
text = font.render('Роман - номер один', 1, RED, WHITE)
text_2 = font.render('Roman and Daria', 0, WHITE, RED)

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # 3. прикрепляем текст на экран(что передаем, координаты(x, y)
    screen.blit(text, (0, 0))
    screen.blit(text_2, (50, 70))

    # 4. выводим на экран, обновляя его
    pygame.display.update()


# ------------------------------------------ COMMENTS ------------------------------------------

# 1. В КОНСОЛЬ PYTHON ИМПОРТИРУЕМ PYGAME, ПИШЕМ - a = pygame.font.get_fonts()
# 2. В ПЕРЕМЕННУЮ ВЫВОДЯТСЯ ВСЕ СИСТЕМНЫЕ ШРИФТЫ