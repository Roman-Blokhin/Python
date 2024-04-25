from logics import *
import pygame
import sys
from database import get_best, cur  # 30. импортируем данные


# 31. функция для отображения топовых игроков
def draw_top_gamers():
    # 31.1 главный текст
    font_top = pygame.font.SysFont('simsun', 30)
    text_top = font_top.render('Total:', True, COLOR_TEXT)
    screen.blit(text_top, (300, 5))

    # 31.2 текст для игроков
    font_top_gamers = pygame.font.SysFont('simsun', 20)
    # 31.4 обходим коллекцию из БД с указанием индекса и имен
    for index, gamer in enumerate(GAMERS_DB):  # 31.5 enumerate выводит сначала индекс, а потом значение
        name, score = gamer  # 31.6 распаковали кортеж, убрали все скобки и кавычки
        # 31.7 делаем динамичный текст для вывода победителей
        s = f'{index}.{name}: {score}'
        text_top_gamers = font_top_gamers.render(s, True, COLOR_TEXT)
        screen.blit(text_top_gamers, (300, 35 + 22 * index))  # 31.7 используем 35 + 22 * index, чтобы выводились игроки

        print(index, name, score)


# 17. Переносим всю отрисовку интерфейса в функцию
def draw_interface(score, delta=0):  # 29.0 дописываем в аргументы дельту, внизу кода тоже при выводе в цикле
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    # 14. создаем шрифт для отображения цифр на нашем игровом поле - название и размер
    font = pygame.font.SysFont('Comic Sans MS', 70)
    # 26. делаем еще один шрифт для отображения очков
    font_score = pygame.font.SysFont('simsun', 48)
    # 29. делаем шрифт для вывода новой цифры из delta
    font_delta = pygame.font.SysFont('simsun', 28)
    text_score = font_score.render('Score: ', True, COLOR_TEXT)  # 26.2 параметры текста очков
    text_score_value = font_score.render(f'{score}', True, COLOR_TEXT)  # 27.1 параметры очков
    screen.blit(text_score, (20, 35))  # 26.3 вывод на экран
    screen.blit(text_score_value, (175, 35))  # 27.2 вывод на экран очков
    # 29.1 условие вывода дельты на экран
    if delta > 0:
        text_delta = font_delta.render(f'+{delta}', True, COLOR_TEXT)
        screen.blit(text_delta, (175, 10))
    else:
        text_delta = font_delta.render(f'+0', True, COLOR_TEXT)
        screen.blit(text_delta, (175, 10))
    # 15. Передвинули вывод массива в консоль перед отрисовкой игры, чтобы не было опоздания
    pretty_print(mas)
    # 32. выводим функцию топовых игроков
    draw_top_gamers()
    # 13. рисуем квадраты игрового поля
    for row in range(BLOCK):
        for column in range(BLOCK):
            # 14.1 находим значение ,которое хранится в массиве
            value = mas[row][column]
            # 14.2 прописываем, что будем писать и как
            text = font.render(f'{value}', True, BLACK)  # значение, обтекание шрифта и цвет
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = (row * SIZE_BLOCK + (row + 1) * MARGIN) + 110
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))  # 16.1 меняем цвет ячейки
            # в соответствии со значением из словаря COLORS
            # 14.3 условие для вывода значения на квадрате
            if value != 0:
                font_w, font_h = text.get_size()  # 14.4 узнаем размер текста
                text_x = w + (SIZE_BLOCK - font_w) / 2  # 14.5 координата размещение текста в квадрате по Х
                text_y = h + (SIZE_BLOCK - font_h) / 2  # 14.6 координата размещение текста в квадрате по У
                screen.blit(text, (text_x, text_y))  # 14.7 размещаем текст на экране по координатам


# 1. создаем двухмерный массив. он проиндексирован. у каждого эл. 2 индекса
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# 26.1 текст вывода очков на экран
COLOR_TEXT = (255, 127, 0)

# 16. создаем словарь для того ,чтобы раскрасить наши ячейки по значению в массиве
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 128, 0),
    32: (255, 0, 128),
    64: (128, 0, 0),
    128: (255, 0, 0),
    256: (128, 128, 255),
    512: (155, 128, 128),
    1024: (0, 128, 255),
    2048: (0, 128, 0),
}

# 10. прописываем константы и переменные
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)

BLOCK = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCK * SIZE_BLOCK + MARGIN * (BLOCK + 1)
HEIGHT = WIDTH + 110
score = 0  # 27. заводим переменную для очков и передаем ее во все наши функции draw_interface(score)
USERNAME = None  # 36.1 константа имени пользователя

# 31.3 переменная для сохранения 3 лучших игроков
GAMERS_DB = get_best()

# 11. пишем визуал на pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)  # 11.1 задаем координаты прямоугольника

# 2. мы можем положить определенные числа в наши ячейки. берем индекс эл. по Х и У

mas[1][2] = 2
mas[3][0] = 2

print(get_empty_list(mas))
pretty_print(mas)

# 30. выводим всех лучших игроков сначала в консоль
for gamer in get_best():
    print(gamer)


# 32. делаем заставку перед началом игры
def draw_intro():
    img2048 = pygame.image.load('2048_logo.png')  # 32.1 загружаем в переменную картинку
    # 33 шрифт и приветственный текст
    font_welcome = pygame.font.SysFont('Comic Sans MS', 50)
    text_welcome = font_welcome.render('Welcome', True, WHITE)
    # 34 создаем текст, который будет вводить пользователь
    name = 'Введите имя'
    is_find_name = False  # 37 переменная, которая будет завершать наш цикл

    # 32.2 делаем цикл обработки событий
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            # 35 делаем возможность добавлять буквы к нашему тексту имени
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():  # 35.1 если нажатая клавиша(unicode), то буква(isalpha)..
                    if name == 'Введите имя':  # 37.2 если надпись "Введите имя", то новая буква затирает ее
                        name = event.unicode
                    else:
                        name += event.unicode  # 35.2 прибавляем букву
                elif event.key == pygame.K_BACKSPACE:  # 35.3 если нажат бекспейс
                    name = name[:-1]  # 35.4 делаем срез, который удаляет последнюю букву
                elif event.key == pygame.K_RETURN:  # 36 нажатие на enter и сохранение имя пользователя в переменную
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True

        screen.fill(BLACK)  # 35.3 заливаем экран черным, чтобы он обновлялся после введения буквы

        # 34.1 Размещаем на экране имя игрока
        text_name = font_welcome.render(name, True, WHITE)
        rect_name = text_name.get_rect()  # 34.2 узнаем размер текста
        rect_name.center = screen.get_rect().center  # 34.3 подменяем координаты надписи и экрана
        screen.blit(text_name, rect_name)  # 34.4 размещаем текст по координатам в rect_name

        # 32.3 прикрепляем картинку к экрану, указываем уменьшение размера, координаты и обновляем экран
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        # 33.1 выводим приветственную надпись
        screen.blit(text_welcome, (240, 75))

        pygame.display.update()
    screen.fill(BLACK)  # 37.1 обновления фона после ввода имени


# 32.4 отрисовываем заставку
draw_intro()


draw_interface(score)  # 17.2 вставляем функцию отрисовки интерфейса
pygame.display.update()  # 17.3 обновляем экран перед циклом, сразу игра будет видна


# 38 создаем цикл для окна game over, он похож с приветственным окном
def draw_game_over():
        img2048 = pygame.image.load('2048_logo.png')
        font_game_over = pygame.font.SysFont('Comic Sans MS', 50)
        text_game_over = font_game_over.render('Game Over', True, WHITE)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            screen.fill(BLACK)
            screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
            screen.blit(text_game_over, (220, 75))
            pygame.display.update()

# 8. Создаем цикл игры
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():  # 12.1 обработка события - закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # 12.2 обработка события - нажатие на любую клавишу
            delta = 0  # 28.4 обнуляем наши очки
            # 19. подключаем функцию обработки события при нажатии кнопки влево на клавиатуре
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)  # 28.3 добавляем переменную дельта для корректности
            # 21. подключаем функцию обработки события при нажатии кнопки вправо на клавиатуре
            if event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            # 23. подключаем функцию обработки события при нажатии кнопки вверх на клавиатуре
            if event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            # 25. подключаем функцию обработки события при нажатии кнопки вниз на клавиатуре
            if event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta  # 28.5 суммируем очки

            # 38.1 дополнительная проверка, чтобы цикл заканчивался корректно, если при нажатии нет вариантов
            if is_zero_in_mas(mas):
                # 12.3 переносим данные цикла в это условие
                # input()
                empty = get_empty_list(mas)  # 8.1 переменная, которая принимает список пустых ячеек
                random.shuffle(empty)  # 8.2 перемешивает элементы массива
                random_num = empty.pop()  # 8.3 удаляет последний элемент списка и возвращает его в переменную num
                x, y = get_index_from_number(random_num)  # 8.4 получаем координаты нашего числа
                mas = insert_2_or_4(mas, x, y)  # 8.5 присваиваем по этим координатам 2 или 4 в ячейку
                print(f'Заполнен элемент под номером: {random_num}. Координаты: {x}, {y}')

            draw_interface(score, delta)  # 17.1 вставляем функцию отрисовки интерфейса после добавления нового элемента
            pygame.display.update()  # подвинули внутрь цикла, чтобы обновление только при нажатии клавиши сразу
        # print(USERNAME)

draw_game_over()
# ----------------------------- COMMENTS ----------------------------
# массив можно писать в таком виде: mas_2 = [[0]*4 for i in range(4)]
