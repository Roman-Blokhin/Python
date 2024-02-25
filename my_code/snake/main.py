import pygame

FRAME_COLOR = (0, 255, 204)  # 7. window color

size = [400, 600]  # 1. переменная с размерами для окна


# 2. создаем окно для игры
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')  # 3. создаем заголовок окна


# 4. делаем цикл, который обрабатывает каждое событие в открытом окне
while True:
    for event in pygame.event.get():  # 5. для каждого получаемого события(клик на клавишу, мышку, крестик и т.д.)
        if event.type == pygame.QUIT:  # 6. если это крестик, то выход
            print('exit')
            pygame.quit()

    # 8. создаем заливку нашего окна
    screen.fill(FRAME_COLOR)
    pygame.display.flip()  # 9. экран переворачивается к нам лицом и мы видим результат работы
