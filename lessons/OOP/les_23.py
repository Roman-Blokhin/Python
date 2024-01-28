# ООП 21 Магический метод __call__ Делаем экземпляры вызываемыми. Callable instance Python

class Counter:
    def __init__(self):
        self.count = 0
        self.summa = 0
        self.length = 0
        print(f'New object: {self}')

    def __call__(self, *args, **kwargs):
        self.count += 1
        self.summa += sum(args)  # считает сумму аргументов, прибавляя к уже имеющимся аргументам
        self.length += len(args)  # считает количество аргументов, прибавляя к уже имеющемуся количеству аргументов
        return f'Счетчик вызван {self.count} раз'

    def average(self):
        return self.summa / self.length

a = Counter()
a(1, 2, 3, 4)
print('Вызвана функция:', a.count)
print('Сумма:', a.summa)
print('Длина:', a.length)
a(6, 90)
print('Вызвана функция:', a.count)
print('Сумма:', a.summa)
print('Длина:', a.length)

print(a.average())  # находим среднее значение