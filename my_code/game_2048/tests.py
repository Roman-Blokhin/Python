# ФАЙЛ ДЛЯ ТЕСТОВ ПРОГРАММЫ

import unittest  # 1. импортируем модуль для проведения тестов
from main import get_number_from_index  # 2. импортируем функцию для проверки из др. файла

# 3. создаем класс проверки, наследуем от unittest.TestCase
class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 8)  # 4. проверяем функцию на равенство