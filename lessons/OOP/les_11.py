# ООП Python 11 Декоратор Property (Property decorator)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property  # 2. декоратор позволяет использовать одно и то же имя для метода и свойства
    def my_balance(self):
        print('get')
        return self.__balance

    @my_balance.setter  # 3. навешиваем декоратор, обращенный к нашей функции геттер
    def my_balance(self, value):  # 4. меняем название метода на название геттера, иначе декоратор не сработает
        print('set')
        if not isinstance(value, (int, float)):
            raise ValueError('Недопустимое значение')
        self.__balance = value

    @my_balance.deleter  # 5. навешиваем декоратор делитера
    def my_balance(self):  # 6. переименовываем метод под название геттера
        print('del')
        del self.__balance

    # 1. мы прописываем свойство - property, централизованно, через переменную
    # my_balance = property(get_balance)  # геттер можно прописать сразу
    # my_balance = my_balance.setter(set_balance)  # сеттер
    # my_balance = my_balance.deleter(delete_balance)  # делитер

a = BankAccount('toy', 100)
print('1.', a.my_balance)  # геттер
a.my_balance = 700  # сеттер
print('2.', a.my_balance)
del a.my_balance  # делитер
a.my_balance = 1
print('3.', a.my_balance)

