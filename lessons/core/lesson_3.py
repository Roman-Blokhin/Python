# РАЗЛИЧНЫЕ ВСТРОЕННЫЕ ФУНКЦИИ

# 1. join - объединение строк с назначаемым разделителем
print('1.')
word = 'romanisagoodperson'
print(' '.join(word))

list_1 = ['eggs', 'bread', 'milk']
food = ', '.join(list_1)  # делаем просто строку из элементов списка
print(list_1)  # начальный вариант
print(food)  # готовый вариант

# 2. replace - замена подстроки на другую подстроку
print('2.')

phrase = 'Hello world'
print(phrase.replace('world', 'Roman'))

# 3. startswith and endswith - проверяют, есть ли подстрока в начале и в конце, выводит булевое значение
print('3.')

a = 'Hello Mr Brown'
print(a.startswith('Hello'))
print(a.endswith('Brown'))
print(a.endswith('Roman'))

