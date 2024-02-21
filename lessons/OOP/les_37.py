# OOP 37 Инструкция raise Возбуждение / Вызов исключений в Python. Raising Exceptions Python

try:
    1/0
except ZeroDivisionError as err:  # 1. мы можем присваивать имя
    print('На ноль делить нельзя')
    print(f'Logging error: {repr(err)}')  # 2. можем к этому имени обращаться, чтобы понять суть ошибки