# ООП 29 Делегирование в Python. Функция super(). Delegating methods in Python

class Person:

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):

    def breathe(self):
        super().breathe()  # 1. Мы можем вызвать родительский метод в дочернем методе
        print('Доктор дышит')


p = Person()
d = Doctor()

d.breathe()  # 1.1 для вызова будет использоваться только одна строчка


class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Settler(User):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)  # 2. чтобы не было повторения кода, лучше вызывать перед новыми атрибутами
        self.age = age


a = User('Roman', 'Romanovich')
b = Settler('Toy', 'Toyevich', 45)

print(a.name, a.surname)
print(b.name, b.surname, b.age)
