# Перемещение текста по экрану

import pygame

pygame.init()

RED = (150, 0, 0)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = (500, 500)
FPS = 60  # 5. частота кадров в секундах, говорит о скорости обновления экрана

# 1. задаем координаты для нашего текста
x_1, y_1 = 0, 0
x_2, y_2 = 150, 170
# 2. создаем переменную для установки скорости изменения кадров в секунду
clock = pygame.time.Clock()
# 8. создаем переменные для перемещения объекта по оси х и у
direct_x_1 = 1
direct_y_1 = 1

# 12. создаем изменение координат для второго объекта
direct_x_2 = 2
direct_y_2 = 2

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Second lesson')
img = pygame.image.load('logo.png')
pygame.display.set_icon(img)

font = pygame.font.SysFont('Comic Sans MS', 36)
text = font.render('Роман - номер один', 1, RED, WHITE)
# 11. узнаем размер нашего объекта
width_1, height_1 = text.get_size()
text_2 = font.render('Roman and Daria', 0, WHITE, RED)
# 13. узнаем размер нашего второго объекта
width_2, height_2 = text_2.get_size()

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(FPS)  # 4. частота кадров в секунду

    screen.fill(BLACK)  # 6. мы обновляем экран, перезаливаем его черным цветом, ставится в начало
    screen.blit(text, (x_1, y_1))
    screen.blit(text_2, (x_2, y_2))
    x_1 += direct_x_1  # 3. изменяем координату х
    y_1 += direct_y_1  # 7. изменяем координату y
    x_2 += direct_x_2
    y_2 += direct_y_2

    if x_1+width_1 >= 500 or x_1 == 0:  # 9. условие разворачивает наш объект обратно по оси x, учитывая ширину
        direct_x_1 = -direct_x_1
    if y_1+height_1 >= 500 or y_1 == 0:  # 10. условие разворачивает наш объект обратно по оси y, учитывая ширину
        direct_y_1 = -direct_y_1

    if x_2+width_2 >= 500 or x_2 == 0:
        direct_x_2 = -direct_x_2
    if y_2+height_2 >= 500 or y_2 == 0:
        direct_y_2 = -direct_y_2

    pygame.display.update()
