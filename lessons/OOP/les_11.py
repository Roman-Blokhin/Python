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

    bal = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
