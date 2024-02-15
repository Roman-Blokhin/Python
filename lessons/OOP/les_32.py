# ООП 32 Slots в Python. __slots_ python - ограничение атрибутов

from timeit import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')  # мы создали коллекцию атрибутов, других атрибутов быть не может

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = PointSlots(3, 4)
b = Point(3, 4)

print(a.y, a.x)

a.y = 50  # можем менять значение атрибута, который есть в нашей коллекции

print(a.y)

del a.y  # можем удалять атрибут

print(a.__slots__)  # для проверки атрибутов в классе используем теперь не __dict__, а __slots__

a.y = 500  # можем добавлять атрибут из коллекции заново, присваивая ему значение

print(a.y)

# Когда у нас есть ограничение атрибутов, то памяти этот класс занимает меньше
print(a.__sizeof__())  # здесь нет атрибута __dict__, поэтому памяти меньше занимает
print(b.__sizeof__(), b.__dict__.__sizeof__())

# операции производятся быстрее, где есть атрибут __slots__
def make_cl1():
    c = Point(3, 4)
    c.x = 100
    c.x
    del c.x

def make_cl2():
    d = PointSlots(3, 4)
    d.x = 100
    d.x
    del d.x

print(timeit(make_cl1))  # смотрим сколько времени нужно на обработку функции, здесь меньше, потому что нет __slots__
print(timeit(make_cl2))