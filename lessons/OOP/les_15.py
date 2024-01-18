# Практика по методам и свойствам (property)

class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password  # 1. аргумент должен быть защищенным/приватным

    @property  # 2. делаем свойство - геттер
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

