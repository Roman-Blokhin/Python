# ООП 28 Наследование. Расширение класса в Python. Extending python class in Python

class Person:

    def breathe(self):
        print('Человек дышит')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walking'):  # 3. проверка, есть ли такой атрибут в родительском классе
            self.walking()


class Doctor(Person):

    def breathe(self):  # 1. переопределение существующего атрибута в родительском классе
        print('Доктор дышит')

    def walking(self):  # 2. расширение родительского класса в дочернем классе
        print('Доктор гуляет')


a = Person()
a.breathe()
a.combo()

print('-'*20)

b = Doctor()
b.breathe()
b.combo()