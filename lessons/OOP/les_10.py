# ООП 10 Геттеры и сеттеры, property атрибуты

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # 1. сделали атрибут приватным, напрямую не обратиться

    def get_balance(self):  # 2. обращаемся к приватному атрибуту через метод
        return self.__balance

    def set_balance(self, value):  # 3. устанавливаем новое значение приватному атрибуту
        if not isinstance(value, (int, float)):  # 4. проверка, принадлежит ли новое значение к числу или флоат
            raise ValueError ('Недопустимое значение')
        self.__balance = value

    # 5. мы прописали свойство, которое помогает нам использовать геттер и сеттер для вывода баланса и его изменения
    bal = property(fget=get_balance, fset=set_balance)


a = BankAccount('Roman', 100)
print('начальный баланс:', a.get_balance())
a.set_balance('200')
print('измененный баланс:', a.get_balance())