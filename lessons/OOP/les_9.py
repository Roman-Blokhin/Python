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