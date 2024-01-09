# ООП 10 Геттеры и сеттеры, property атрибуты

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # 1. сделали атрибут приватным, напрямую не обратиться

    def get_balance(self):  # 2. обращаемся к приватному атрибуту через метод
        print('get')
        return self.__balance

    def set_balance(self, value):  # 3. устанавливаем новое значение приватному атрибуту
        print('set')
        if not isinstance(value, (int, float)):  # 4. проверка, принадлежит ли новое значение к числу или флоат
            raise ValueError ('Недопустимое значение')
        self.__balance = value

    def delete_balance(self):  # 6. добавил метод удаления и прописал делитер в проперти
        print('del')
        del self.__balance

    # 5. мы прописали свойство, которое помогает нам использовать геттер и сеттер для вывода баланса и его изменения
    bal = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


a = BankAccount('Roman', 100)
print('начальный баланс:', a.get_balance())
# a.set_balance('200')
print('измененный баланс:', a.get_balance())

s = BankAccount('Rob', 100)
print(s.bal)
s.bal = 800
print(s.bal)