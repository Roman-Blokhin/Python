# ООП 30 Множественное наследование в Python. Multiple inheritance in Python

class Doctor:
    def can_care(self):
        print('Я - Доктор, могу лечить')

    def can_build(self):  # 2. если в обоих классах есть методы с одним названием, то будет важен порядок наследования
        print('Я - Доктор, я тоже могу немного строить')

    def graduate(self):
        print("Я отучился на Доктора")


class Builder:
    def can_build(self):
        print('Я - Строитель, могу строить')

    def graduate(self):
        print("Я отучился на Строителя")


class Person(Doctor, Builder):  # 1. можно наследоваться от нескольких классов, важен порядок
    def graduate(self):  # 4. проверяем ,какой метод у нас вызовется
        print("Посмотрите, кем я стал")
        super().graduate()
        Builder.graduate(self)  # 4.2 но мы можем вызвать отдельно метод у второго родительского класса


a = Person()
a.can_build()  # 2.1 метод доктора вызывается, потому что он первый в списке наследования у класса Person

print(Person.__mro__)  # 3. мы можем посмотреть порядок наследования и поиска информации в классах

a.graduate()  # 4.1 вызывается только доктор, потому что из-за повтора кода мы ограничиваем повторение - super()


# --------------------------------------------

# 5. если у нас есть одинаковые методы с разными значениями

class Orc:
    def __init__(self, job):
        self.job = job


class Elf:
    def __init__(self, work):
        self.work = work


class User(Elf, Orc):
    def __init__(self, job, work):  # 5.1 простой способ вывести все параметры родительских классов
        self.job = job
        self.work = work

    def __str__(self):  # 5.2 помогает вывести на экран корректно
        return f'User: {self.job}, {self.work}'


b = User('Fisher', 'Backer')

print(b)  # 5.3 выводим результат экземпляра User

# --------------------------------------------

# 6. убираем повторный код

class Orc_1:
    def __init__(self, rank):
        self.rank = rank


class Elf_1:
    def __init__(self, prof):
        self.prof = prof


class User_1(Elf_1, Orc_1):
    def __init__(self, rank, prof):
        super().__init__(prof)  # 6.1 Делегирование - прописываем атрибут от первого родительского класса в списке
        Orc_1.__init__(self, rank)  # 6.2 Делегирование

    def __str__(self):
        return f'User_1: {self.rank}, {self.prof}'


q = User_1('Instructor', 'Teacher')

print(q)