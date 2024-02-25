import pygame

FRAME_COLOR = (0, 255, 204)  # 7. window color
WHITE = (255, 255, 255)  # 10. rect color

SIZE_BLOCK = 20  # 12. rectangle's size
COUNT_BLOCKS = 20  # 13. сколько у нас будет квадратиков на экране

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

    # 11. рисуем квадратики нашего поля(место, цвет, [расположение и размер квадрата])
    pygame.draw.rect(screen, WHITE, [10, 20, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()  # 9. экран переворачивается к нам лицом и мы видим результат работы
