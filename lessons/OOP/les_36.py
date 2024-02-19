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

# 3. исключения это классы, поэтому можно обрабатывать их, указывая на родительский класс
# к примеру: lookupError = IndexError and KeyError

s = 'hello'

try:
    print(s[8])
except LookupError:  # родительский класс исключения
    print('LookupError')

try:
    print(s[8])
except IndexError:  # 2. дочерний класс
    print('IndexError')
except LookupError:
    print('LookupError')
