# ООП 9 Публичные, приватные, защищенные атрибуты и методы Python Public Protected Private

# 1. публичные данные, все можно спокойно вызвать и посмотреть
class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def print_account(self):
        print(self.name, self.balance, self.password)

account_1 = BankAccount('Bob', 100000, '1234')
account_1.print_account()  # получаем данные внутри банка

print(account_1.name)  # получаем данные ВНЕ банка
print(account_1.balance)
print(account_1.password)

print('2 --------------------')

# 2. защищенные данные, используются на уровне разработки для согласования(для нужд внутри класса)
class BankAccount_2:
    def __init__(self, name, balance, password):
        self._name = name
        self._balance = balance
        self._password = password

    def print_protected_account(self):
        print(self._name, self._balance, self._password)

account_2 = BankAccount_2('Bob', 100000, '1234')
account_2.print_protected_account()

print(account_2._name)
print(account_2._balance)
print(account_2._password)

print('3 --------------------')

# 3. приватные данные, можно внутри класса, но нельзя ВНЕ класса(инкапсуляция - сокрытие данных)
class BankAccount_3:
    def __init__(self, name, balance, password):
        self.__name = name
        self.__balance = balance
        self.__password = password

    def print_private_account(self):
        print(self.__name, self.__balance, self.__password)

account_3 = BankAccount_3('Bob', 100000, '1234')
account_3.print_private_account()

# print(account_3.__name)  # вне класса уже нельзя вызвать, возникает ошибка
# print(account_3.__balance)
# print(account_3.__password)

print('4 --------------------')

# 4. можно сделать приватными не только атрибуты объекта, но и сам метод
class BankAccount_4:
    def __init__(self, name, balance, password):
        self.__name = name
        self.__balance = balance
        self.__password = password

    def print_public_account(self):  # открытый метод для вызова приватного метода
        self.__print_private_account()

    def __print_private_account(self):  # напрямую приватный метод не вызывается, только через открытый метод
        print(self.__name, self.__balance, self.__password)

account_4 = BankAccount_4('Bob', 100000, '1234')
account_4.print_public_account()
