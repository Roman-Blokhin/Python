# ИГРА КРЕСТИКИ-НОЛИКИ

import pygame

pygame.init()

# ------------------------------------------ VARIABLES ------------------------------------------

FRAME_COLOR = (100, 100, 100)
RED = (255, 0, 0)
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
mas = [[0] * 3 for i in range(count_block)]
# 8. создаем переменную для определения четности нажатия. так поймем, какой игрок ходит
qwerty = 0

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
            # 5. определяем, на какой квадрат мы нажали
            col = x_mouse // (block_size + margin)
            row = y_mouse // (block_size + margin)
            # 9. замена в ячейке может быть только, если ее значение равно 0
            if mas[row][col] == 0:
                # 8.1 определяем четность нажатия
                if qwerty % 2 == 0:
                    # 6. присваиваем этому квадрату значение
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'y'
                # 8.2 увеличиваем переменную на 1
                qwerty += 1

    clock.tick(FPS)
    screen.fill(FRAME_COLOR)

    # 1. прописали цикл вывода квадратов игрового поля
    for row in range(count_block):
        for col in range(count_block):
            # 7. используем значение квадрата для определения цвета при нажатии
            if mas[row][col] == 'x':
                color = GREEN
            # 8.3 делаем проверку на четность игрока для понимания цвета нажатия на квадрат
            elif mas[row][col] == 'y':
                color = RED
            else:
                color = WHITE

            x = col * block_size + margin * (col + 1)
            y = row * block_size + margin * (row + 1)
            pygame.draw.rect(screen, color, (x, y, block_size, block_size))

            # 10. рисуем крестики и нолики в квадратах
            if color == GREEN:  # 10.1 делаем крестик из двух линий в зеленом квадрате
                pygame.draw.line(screen, WHITE, (x + 15, y + 15), (x + block_size - 15, y + block_size - 15), 5)
                pygame.draw.line(screen, WHITE, (x + block_size - 15, y + 15), (x + 15, y + block_size - 15), 5)
            elif color == RED:  # 10.2 делаем нолик из круга в красном квадрате
                pygame.draw.circle(screen, WHITE, (x + block_size // 2, y + block_size // 2), block_size // 2 - 10, 5)

    pygame.display.update()
