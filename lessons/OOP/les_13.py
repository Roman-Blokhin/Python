# ООП 13 Класса-методы (сlassmethod) и статические методы (staticmethod)

class Example:
    def hello():  # 1. функцию можно вызвать только от класса
        print('hello')

    def instance_hello(self):  # 2. функцию можно вызвать только от экземпляра
        print('instance_hello')

    @staticmethod  # 3. навешиваем декоратор, чтобы функцию можно было вызывать и от класса, и от экземпляра
    def static_hello():  # 4. функцию можно вызвать только от экземпляра
        print('static_hello')

    @classmethod
    def class_hello(cls):  # 5. функцию можно вызвать от целого класса
        print('class_hello')