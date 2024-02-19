# OOP 36 Обработка исключений Try Except Finally Python

# 1. срабатывает обработка первого исключения и программа прерывается
try:
    a+b
    print('roman')
    1/0
    int('hello')
except NameError:  # 3. обработка исключений идет сверху вниз
    print('NameError')
except ValueError:  # 2. исключений может быть несколько
    print('ValueError')

