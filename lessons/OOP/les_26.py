# Наследование в объектно-ориентированном программировании. Введение в ООП Python

class Person:
    def breathe(self):
        print('Я могу дышать')

    def walking(self):
        print('Я могу ходить')


class Doctor(Person):  # наследуем класс Person, чтобы не копировать код в каждый класс
    def iam(self):
        print('Я - доктор')


class Teacher(Person):  # наследуем класс Person, чтобы не копировать код в каждый класс
    def iam(self):
        print('Я - учитель')


# ИСПОЛЬЗУЕМ НАСЛЕДОВАНИЕ КЛАССА, ЧТОБЫ ОДИНАКОВЫЙ КОД НАХОДИЛСЯ В ОДНОМ МЕСТЕ
a = Doctor()

a.iam()
a.breathe()
a.walking()

print('------')

b = Teacher()

b.iam()
b.breathe()
b.walking()
