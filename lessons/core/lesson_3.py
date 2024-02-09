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

# 4. split - преобразует строку в список из отдельных элементов
print('4.')

phrases = 'Do you remember me?'
print('I am going to the museum'.split())
print(phrases.split())

# 5. max and min - находят минимальное и максимальное значение
print('5.')

num = [1, 2, 4, -90, 895, 50, 65]
print(max(num))
print(min(num))

# 5. sum - находит сумму
print('6.')

num = [1, 2, 4, 90, 895, 50, 65]
print(sum(num))

# 6. abs - делает число положительным
print('7.')

print(abs(-900))

# 5. round - округляет число до определенного количества знаков после запятой
print('8.')

n = 12.06594729239875
print(round(n, 2))
print(round(n, 5))



