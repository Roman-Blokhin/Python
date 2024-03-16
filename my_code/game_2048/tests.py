# ФАЙЛ ДЛЯ ТЕСТОВ ПРОГРАММЫ

import unittest  # 1. импортируем модуль для проведения тестов
from main import get_number_from_index, get_empty_list, get_index_from_number  # 2. импортируем функцию из др. файла

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