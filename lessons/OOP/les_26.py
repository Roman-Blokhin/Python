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


class Ortoped(Doctor):
    pass


# ИСПОЛЬЗУЕМ НАСЛЕДОВАНИЕ КЛАССА, ЧТОБЫ ОДИНАКОВЫЙ КОД НАХОДИЛСЯ В ОДНОМ МЕСТЕ
a = Doctor()

a.iam()
a.breathe()
a.walking()

b = Teacher()

b.iam()
b.breathe()
b.walking()

print('2. ------')

# Мы можем проверить, является ли класс чьим-нибудь подклассом

print(issubclass(Doctor, Person))
print(issubclass(Teacher, Person))

print('3. ------')

# Мы можем проверить, принадлежит ли экземпляр к классу

print(isinstance(a, Doctor))
print(isinstance(a, Person))  # спрашиваем про родительский класс
print(isinstance(b, Doctor))

print('4. ------')

# Наследование по цепочки может быть бесконечным: Person - Doctor - Ortoped
# Последний класс будет иметь все свойства предыдущих классов

c = Ortoped()
print(isinstance(c, Person))