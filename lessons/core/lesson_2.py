# СПИСКОВОЕ ВКЛЮЧЕНИЕ - быстрый метод создания списков

# 1. прописываем задание и цикл для выполнения - i в 3 степени для всех чисел от 0 до 5, не включая 5
cubes = [i**3 for i in range(5)]
print(cubes)

# 2. списковое включение также может содержать условие - выводим четные числа
cubes = [i**2 for i in range(10) if i**2 % 2 == 0]
print(cubes)

# 3. очень большие списки не вывести, будет ошибка
# cubes = [i**2 for i in range(10**100)]
# print(cubes)

