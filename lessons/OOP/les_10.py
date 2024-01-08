# ООП 10 Геттеры и сеттеры, property атрибуты

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # 1. сделали атрибут приватным, напрямую не обратиться

    def get_balance(self):  # 2. обращаемся к приватному атрибуту через метод
        return self.__balance

    def set_balance(self, value):  # 3. устанавливаем новое значение приватному атрибуту
        self.__balance = value

a = BankAccount('Roman', 100)
print('начальный баланс:', a.get_balance())
a.set_balance(200)
print('измененный баланс:', a.get_balance())