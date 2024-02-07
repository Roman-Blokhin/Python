# ООП 27 Наследование. Переопределение методов в Python. Method overriding in Python

class Person:
    name = 'Roman'

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')

    def sleep(self):
        print('Человек спит')

    def combo(self):  # 5. мы можем комбинировать методы в один
        self.breathe()
        self.walk()
        self.sleep()


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

# 5.1 проверяем, как вызывается метод combo у класса Doctor, когда 1 метод переопределен, а другие нет
d.combo()


# --------------------------------------------------

class Unit:
    def __init__(self, age):  # 3. фактически мы переопределяем метод __init__, который наследуется у класса object
        print('init Person')
        self.age = age

    def __str__(self):  # 4. делаем значение для всех классов, которые наследуют от Person
        return f'Person: {self.age}'


class Settler(Unit):
    def __str__(self):  # 4.1 переопределяем значение метода, наследуемого из Person
        return f'Doctor: {self.age}'


a = Unit(48)
b = Settler(19)  # 3.1 срабатывает метод __init__ из класса Person

print(a.age, b.age)

# 4.2 поэтому будут выведены разные значения
print(a)
print(b)
