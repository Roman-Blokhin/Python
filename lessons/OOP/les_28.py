# ООП 27 Наследование. Переопределение методов в Python. Method overriding in Python

class Person:
    name = 'Roman'

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

# 2. наследуются не только методы, но и переменные. Переопределить можно также, как и с методами
print(p.name)
print(d.name)