# Практика по методам и свойствам (property)

from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password  # 1. аргумент должен быть защищенным/приватным
        # 1.1 но после установки проверок и свойства @password.setter, обращение должно быть именно как к свойству
        # поэтому мы меняем self.__password на self.password

    @staticmethod  # 5. проверка, содержит ли пароль цифры
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @property  # 2. делаем свойство - геттер
    def password(self):
        print('get')
        return self.__password

    @password.setter  # 3. делаем свойство - сеттер
    def password(self, value):
        print('set')
        if not isinstance(value, str):  # 4. проверяем принадлежность данных к определенному типу
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 3:
            raise ValueError('Пароль не может быть меньше 3 символов')
        if len(value) > 10:
            raise ValueError('Пароль не может быть не больше 10 символов')
        if not User.is_include_digit(value):
            raise ValueError('Пароль должен содержать цифры')
        self.__password = value
