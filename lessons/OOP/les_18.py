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