# игра 2048 на Python Pygame. Прописываем логику игры
import copy
import random
import copy

# 3. функция удобного вывода данных массива в консоль
def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)  # 3.1 знак звездочки делает распаковку, убирает в массиве скобки и запятые
    print('-' * 10)


# 5. функция, которая будет считать каждый элемент массива не по индексу, а по порядку, начиная не с 0, а с 1
def get_number_from_index(i, j):
    return i * 4 + j + 1  # 5.0 для удобства можно нарисовать массив и проиндексировать элементы


# 6. функция, которая по номеру числа возвращает нам координаты
def get_index_from_number(num):
    num -= 1  # 6.1 потому что индекс мы считаем с 1, а не с 0
    x, y = num // 4, num % 4  # 6.2 сначала находим строку, потом столбец
    return x, y


# 4. пробегаемся по всему массиву и смотрим, какое значение еще не заполнено в строках и столбцах и выводим их
def get_empty_list(mas):
    empty = []  # 5.2 пустой список для сохранения всех пустых ячеек в него
    for i in range(4):  # 4.1 проверка по строкам
        for j in range(4):  # 4.2 проверка по столбцам
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)  # 5.1 создаем переменную, по формуле будет искать пустую ячейку
                empty.append(num)  # 5.3 сохраняет все пустые элементы игры
    return empty  # 5.4 возвращаем наш список по окончанию функции


# 7. создаем функцию, которая будет присваивать нам рандомное значение для ячеек: 2 или 4
def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


# 9. функция, которая проверяет, есть ли нули в массиве
def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False


# 18. движение массива влево и схлопывание в нем чисел
def move_left(mas):
    # 28. делаем переменную, которая будет считать очки
    delta = 0
    origin = copy.deepcopy(mas)
    for row in mas:  # 18.1 для строк в массиве
        while 0 in row:  # 18.2 пока есть 0 в строке
            row.remove(0)  # 18.3 удаляем все нули
        while len(row) != 4:  # 18.4 пока в строке не 4 числа
            row.append(0)  # 18.5 добавляем нули в конец списка
    for i in range(4):  # 18.6 пробегаемся по строкам
        for j in range(3):  # 18.7 пробегаемся по столбцам, кроме последнего
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:  # 18.8 если индекс массива = соседнему индексу и не равен 0
                mas[i][j] *= 2  # 18.9 умножаем число по индексу на 2
                delta += mas[i][j]  # 28.1 каждый раз, когда рядом 2 одинаковых числа, увеличиваем наши очки
                mas[i].pop(j + 1)  # 18.10 удаляем соседний индекс
                mas[i].append(0)  # 18.11 добавляем 0 в конец списка
    return mas, delta, not origin == mas


# 20. движение массива вправо и схлопывание в нем чисел
def move_right(mas):
    delta = 0
    origin = copy.deepcopy(mas)
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)  # 20.1 нули вставляем в начало - индекс и значение
    for i in range(4):
        for j in range(3, 0, -1):  # 20.2 обходим колонки справа налево с шагом -1
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:  # 20.3 если индекс массива = соседу слева
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j - 1)  # 20.4 удаляем соседа слева
                mas[i].insert(0, 0)  # 20.5 нули вставляем в начало - индекс и значение
    return mas, delta, not origin == mas


# 22. движение массива вверх и схлопывание в нем чисел
def move_up(mas):
    delta = 0
    origin = copy.deepcopy(mas)
    for j in range(4):  # 22.1 сначала мы обходим колонки
        column = []  # 22.2 создаем побочный список, куда будем добавлять числа(одномерный массив)
        for i in range(4):  # 22.3 проходимся по рядам
            if mas[i][j] != 0:  # 22.4 если в ряду и колонке хранится не нулевой элемент
                column.append(mas[i][j])  # 22.5 то мы помещаем его в наш список
        while len(column) != 4:  # 22.6 пока длина списка не равна 4
            column.append(0)  # 22.7 добавляем в него нули
        for i in range(3):  # 22.8 пробегаемся по элементам
            if column[i] == column[i + 1] and column[i] != 0:  # 22.9 если соседние элементы равны и текущий не = 0
                column[i] *= 2  # 22.10 они схлопываются
                delta += column[i]
                column.pop(i + 1)  # 22.11 удаляем второй элемент
                column.append(0)  # 22.12 добавляем вместо него 0
        for i in range(4):  # 22.13 обходим наши элементы
            mas[i][j] = column[i]  # 22.14 по индексу сохраняем номер элемента в колонке в массив
    return mas, delta, not origin == mas


# 24. движение массива вниз и схлопывание в нем чисел
def move_down(mas):
    delta = 0
    origin = copy.deepcopy(mas)
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i - 1)
                column.insert(0, 0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta, not origin == mas


# 25. игра не заканчивается, когда нулей в массиве уже не осталось, но есть одинаковые элементы по вертикали или гориз.
def can_move(mas):
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] or mas[i][j] == mas[i + 1][j]:  # 25.1 если элемент = соседу справа или снизу
                return True

    for i in range(1, 4):
        for j in range(1, 4):
            if mas[i][j] == mas[i - 1][j] or mas[i][j] == mas[i][j-1]:
                return True

    return False