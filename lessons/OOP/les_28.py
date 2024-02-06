# ООП 27 Наследование. Переопределение методов в Python. Method overriding in Python

class Person:
    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')


class Doctor(Person):
    def breathe(self):  # 1. переопределение родительского метода
        print('Доктор тоже дышит')


p = Person()
d = Doctor()

p.breathe()
d.breathe()  # 1.1 сначала проверяется свой класс на наличие подобных методов, потом уже родительский, если пусто