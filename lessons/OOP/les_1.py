# ООП 1 Классы, объекты, экземпляры классов. Объектно-ориентированное программирование в Python

# пример данных
a = [1, 2, 3]
print(a)
s = 'roman'

# пример действий(встроенный метод)
print (s.upper())

# посмотреть тип данных
print(type(s))
print(type(a))

# проверяем, принадлежит ли определенному классу объект
print(isinstance(4, int))

# создали класс
class Car:
    model = 'BMW'
    engine = 1.4

# присваиваем объект классу
a = Car()
