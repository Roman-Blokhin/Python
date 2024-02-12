# ООП 30 Множественное наследование в Python. Multiple inheritance in Python

class Doctor:
    def can_care(self):
        print('Я - Доктор, могу лечить')

    def can_build(self):  # 2. если в обоих классах есть методы с одним названием, то будет важен порядок наследования
        print('Я - Доктор, я тоже могу немного строить')


class Builder:
    def can_build(self):
        print('Я - Строитель, могу строить')


class Person(Doctor, Builder):  # 1. можно наследоваться от нескольких классов, важен порядок
    pass


a = Person()
a.can_build()  # 2.1 метод доктора вызывается, потому что он первый в списке наследования у класса Person

print(Person.__mro__)  # 3. мы можем посмотреть порядок наследования и поиска информации в классах
