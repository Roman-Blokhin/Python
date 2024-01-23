# ООП 17 Магические методы __add__, __mul__, __sub__ и __truediv__
# базовые математические вычисления

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # 1. делаем метод сложения нашего баланса с числом
    def __add__(self, other):
        if isinstance(other, (int, float)):  # 2. проверка, принадлежит ли наш аргумент к типам (int, float)
            return self.balance + other
        if isinstance(other, BankAccount):  # 3. позволяет сложить объект с объектом и получить общи баланс
            return self.balance + other.balance
        raise NotImplemented  # 4. если проверки не проходят, мы не можем сделать вычисление

    # 6. умножение
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented

    def __radd__(self, other):  # 5. позволяет избежать ошибки, когда число складываем с объектом self - (12 + w)
        return self + other  # 5.1 меняет местами объекты для корректного сложения
