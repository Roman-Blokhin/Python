# Практика по методам и свойствам (property)

from string import digits

lister = ['qwerty1234', '12345', '1234567890', 'ytrewq', '0987654321']


class User:
    global lister

    def __init__(self, login, password):
        self.login = login
        self.password = password  # 1. аргумент должен быть защищенным/приватным
        # 1.1 но после установки проверок и свойства @password.setter, обращение должно быть именно как к свойству
        # поэтому мы меняем self.__password на self.password
        self.__secret = 'abracadabra'  # 7. установили секретный аргумент для определенного доступа

    @property
    def secret(self):
        s = input('Введите пароль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт')

    @staticmethod  # 5. проверка, содержит ли пароль цифры
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod  # 6. проверка, на простоту пароля из списка
    def is_include_lister(password):
        for i in lister:
            if i in password:
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
        if not User.is_include_digit(value):  # 5.1
            raise ValueError('Пароль должен содержать цифры')
        if User.is_include_lister(value):  # 6.1
            raise ValueError('Слишком простой пароль')
        self.__password = value
