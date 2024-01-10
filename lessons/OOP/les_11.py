# ООП Python 11 Декоратор Property (Property decorator)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get')
        return self.__balance

    def set_balance(self, value):
        print('set')
        if not isinstance(value, (int, float)):
            raise ValueError('Недопустимое значение')
        self.__balance = value

    def delete_balance(self):
        print('del')
        del self.__balance

    # 1. мы прописываем свойство - property, централизованно, через переменную
    my_balance = property(get_balance)  # геттер можно прописать сразу
    my_balance = my_balance.setter(set_balance)  # сеттер
    my_balance = my_balance.deleter(delete_balance)  # делитер


