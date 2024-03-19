# игра 2048 на Python Pygame. Прописываем логику игры
import random

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
    pass