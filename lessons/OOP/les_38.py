# OOP 38 Пользовательские исключения в Python Custom Exception Python

class MyExcept(Exception):
    def __init__(self, *args):  # 4. передаем любое количество аргументов
        if args:
            self.message = args[0]  # 5. сохраняем все под индексом ноль, соответственно будет 1 аргумент только
        else:
            self.message = None

    def __str__(self):  # 6. описываем вывод в консоли
        if self.message:
            return f'Message ({self.message})'
        else:
            return 'Message is empty'

raise MyExcept('roman', 'toy', 789)

# ---------------------------------------- 2 -------------------------------------------

class MyException(Exception):  # 1. все наследуется от класса исключений Exception
    """roman is a hero"""


try:
    raise MyException('1', '2', 'hello')  # 2. мы можем, обрабатывая исключение, передавать в него аргументы
except:
    print('done')

# ----------------------------------------

try:
    raise MyException('1', '2', 'hello')
except AttributeError:  # 3. не входит в class Exception, поэтому исключение не обрабатывается
    print('done')


