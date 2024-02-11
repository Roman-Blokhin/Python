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

# ------------------------------------------------------

class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'  # 3 будет self от класса Doctor, если через него вызывать

    def info(self):
        print('Parent class')
        print(self)  # 3.1 будет self от класса Doctor, если через него вызывать


class Settler(User):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)  # 2. чтобы не было повторения кода, лучше вызывать перед новыми атрибутами
        self.age = age  # 2.1 писать после super(), чтобы значение не перезаписывалось

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'


a = User('Roman', 'Romanovich')
b = Settler('Toy', 'Toyevich', 45)

print(a.name, a.surname)
print(b.name, b.surname, b.age)

a.info()
b.info()  # вызывет self от Doctor
