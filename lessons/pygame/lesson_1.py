# Первая программа на pygame

import pygame

size = (400, 400)  # 1.1 размер окна

pygame.display.set_mode(size)  # 1. создание экрана
pygame.display.set_caption('The first program')  # 2. заголовок
img = pygame.image.load('logo.png')  # 3. пишем путь к логотипу
pygame.display.set_icon(img)  # 4. загружаем логотип

# 5. цикл, чтобы программа не закрывалась
while True:
    for event in pygame.event.get():  # 6. мы перехватываем все события, которые производятся в программе
        if event.type == pygame.QUIT:  # 7. если событие - нажатие на крестик, то выход
            pygame.quit()
