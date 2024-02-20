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
except IndexError:  # дочерний класс
    print('IndexError')
except LookupError:
    print('LookupError')

# 4. если мы не указываем название исключения, то будут обрабатываться все исключения без опознания
try:
    print(s[8])
except:
    print('Error')
# 5. блок, который обрабатывается всегда после обработки исключений, только 1 раз, помогает в работе с файлами
finally:
    print('Roman number one')

# 6. можно использовать else, но должен быть хотя бы 1 except, сработает, если в try нет ошибок(исключений)
try:
    1/5
except (IndexError, KeyError):
    print('Error')
else:  # сработает, если не сработало исключение
    print('good')
finally:
    print('Roman the first')


