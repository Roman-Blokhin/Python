# ИГРА КРЕСТИКИ-НОЛИКИ

import pygame
pygame.init()

# ------------------------------------------ FUNCTIONS ------------------------------------------

# 11. пишем функцию, которая определяет, кто выиграл
def win(mas, sign):
    # 12. на случай ничьи, когда все клетки заполнены, но никто не победил
    zeroes = 0  # 12.1 переменная для подсчета незаполненных клеток

    # 11.1 цикл для проверки строк
    for row in mas:
        # 12.2 находим количество нулей в ряду и прибавляем к zeroes
        zeroes += row.count(0)

        if row.count(sign) == 3:
            return sign

    # 11.2 цикл для проверки колонок, можем проверять только по индексу
    for col in range(3):  # 11.3 если индекс в колонке равен следующему индексу в этой же колонке и т.д.
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign

    # 11.3 проверяем главную диагональ(слева направо)
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign

    # 11.4 проверяем побочную диагональ(справа налево)
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign

    # 12.3 проверяем, есть ли пустые клетки в нашем массиве
    if zeroes == 0:
        return 'Piece'

    # 11.5 если ни одно условие не выполняется, возвращаем false
    return False

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

# 15. устанавливаем начальное значение конца игры
game_over = False

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
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # 15.1 and not game_over - реагирование на клик
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

    # 15.3 отрисовка игры должна быть, когда сама игра не закончена
    if not game_over:
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

    # 13. нужно понять, какой игрок сейчас ходит, чтобы применить функцию
    if (qwerty-1) % 2 == 0:  # 13.1 так как мы уже увеличили qwerty на 1 в цикле и поменяли игрока, возвращаем значение
        game_over = win(mas, 'x')  # 13.2 передаем значение 1 игрока - х
    else:
        game_over = win(mas, 'o')  # 13.3 передаем значение 2 игрока - о

    # 14. прописываем условие на конец игры
    if game_over:
        screen.fill(BLACK)  # 14.1 закрашиваем экран черным
        font = pygame.font.SysFont('Comic NS Sans', 60)  # 14.2 создаем шрифт
        text_1 = font.render(game_over, True, WHITE)  # 14.3 текст прописан в переменной game_over
        text_rect = text_1.get_rect()  # 14.4 узнаем координаты текста
        text_x = screen.get_width() // 2 - text_rect.width // 2  # 14.5 прописываем координаты центра экрана по ширине
        text_y = screen.get_height() // 2 - text_rect.height // 2  # 14.6 прописываем координаты центра экрана по выс.
        screen.blit(text_1, [text_x, text_y])  # 14.7 размещаем наш текст, указывая координаты

    pygame.display.update()
