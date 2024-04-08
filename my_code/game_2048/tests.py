# ФАЙЛ ДЛЯ ТЕСТОВ ПРОГРАММЫ

import unittest  # 1. импортируем модуль для проведения тестов
# 2. импортируем функции из др. файла:
from logics import get_number_from_index, get_empty_list, get_index_from_number, is_zero_in_mas, move_left, move_down,\
    move_up, can_move

# 3. создаем класс проверки, наследуем от unittest.TestCase
class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)  # 4. проверяем функцию на равенство

    def test_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)  # 5. проверяем функцию на равенство

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)  # 6. проверяем на наличие пустого массива

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)  # 6. проверяем на наличие части заполненного массива

    def test_5(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)  # 6. проверяем массив на полную заполненность


    def test_6(self):
        self.assertEqual(get_index_from_number(8), (1, 3))  # 7. проверяем число по индексу


    def test_7(self):
        self.assertEqual(get_index_from_number(16), (3, 3))  # 7. проверяем число по индексу


    def test_8(self):
        self.assertEqual(get_index_from_number(1), (0, 0))  # 7. проверяем число по индексу

    def test_9(self):  # 8. проверяем массив на наличие нулей
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_10(self):  # 8. проверяем массив на наличие нулей
        mas = [
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_11(self):  # 8. проверяем массив на наличие нулей
        mas = [
            [1, 0, 1, 1],
            [1, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_12(self):  # 9. принимаем массив и сравниваем с новым, который уже схлопнулся, движение влево
        mas = [
            [2, 4, 2, 2],
            [0, 0, 8, 8],
            [0, 4, 4, 0],
            [0, 0, 0, 8],
        ]

        rez = [
            [2, 4, 4, 0],
            [16, 0, 0, 0],
            [8, 0, 0, 0],
            [8, 0, 0, 0],
        ]
        self.assertEqual(move_left(mas), (rez, 28))  # 28.2 добавляем значение delta для проверки

    def test_13(self):  # 9. принимаем массив и сравниваем с новым, который уже схлопнулся, движение влево
        mas = [
            [2, 2, 8, 0],
            [0, 4, 4, 8],
            [0, 2, 0, 2],
            [4, 4, 2, 0],
        ]

        rez = [
            [4, 8, 0, 0],
            [8, 8, 0, 0],
            [4, 0, 0, 0],
            [8, 2, 0, 0],
        ]
        self.assertEqual(move_left(mas), (rez, 24))


    def test_14(self):  # 10. принимаем массив и сравниваем с новым, который уже схлопнулся, движение вверх
        mas = [
            [2, 8, 2, 4],
            [2, 0, 2, 8],
            [4, 0, 0, 4],
            [4, 8, 2, 4],
        ]

        rez = [
            [4, 16, 4, 4],
            [8, 0, 2, 8],
            [0, 0, 0, 8],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_up(mas), (rez, 40))


    def test_15(self):  # 11. принимаем массив и сравниваем с новым, который уже схлопнулся, движение вниз
        mas = [
            [2, 8, 2, 4],
            [2, 0, 2, 8],
            [4, 0, 0, 4],
            [4, 8, 2, 4],
        ]

        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 4],
            [4, 0, 2, 8],
            [8, 16, 4, 8],
        ]
        self.assertEqual(move_down(mas), (rez, 40))


    def test_16(self):  # 12. проверка на равенство соседних элементов
        mas = [
            [2, 8, 2, 4],
            [2, 0, 2, 8],
            [4, 0, 0, 4],
            [4, 8, 2, 4],
        ]

        self.assertEqual(can_move(mas), True)


    def test_17(self):  # 12. проверка на равенство соседних элементов
        mas = [
            [2, 8, 2, 4],
            [21, 5, 50, 8],
            [4, 44, 90, 4],
            [43, 8, 2, 9],
        ]

        self.assertEqual(can_move(mas), False)