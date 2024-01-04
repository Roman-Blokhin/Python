# ООП 6 Инициализация объекта. Метод init . Объектно-ориентированное программирование в Python.

class Dog:
    def __init__(self, name, color='white', age=1, breed='no'):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed

        print(f'Нашу собаку зовут: {name}, ее цвет: {color}, ее возраст: {age}, а порода у нее: {breed}')

# 1. метод инициализации сразу создает указанные аргументы у экземпляра и передает в них прописанные значения
rob = Dog('ROB', 'Black', 33, 'Tsverg')
print('1')
print(rob.name, rob.color, rob.age, rob.breed)  # вызываем значения аргументов

# 2. если в методе есть значения по умолчанию, а новые значения не прописаны, передаются значения по умолчанию
jim = Dog('Jim', breed='taxa')  # конкретный параметр передается по ключу
print('2')
print(jim.name, jim.color, jim.age, jim.breed)