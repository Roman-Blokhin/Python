# OOP 38 Пользовательские исключения в Python Custom Exception Python

class MyException(Exception):  # 1. все наследуется от класса исключений Exception
    pass

try:
    raise MyException('1', '2', 'hello')  # 2. мы можем, обрабатывая исключение, передавать в него аргументы
except:
    print('done')

# ----------------------------------------

try:
    raise MyException('1', '2', 'hello')
except AttributeError:  # 3. не входит в class Exception, поэтому исключение не обрабатывается
    print('done')