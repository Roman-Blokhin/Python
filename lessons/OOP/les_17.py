# ООП 16 Магические методы __len__ и __abs__. (Dunder methods)

class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):  # 1. мы можем сложить имя и фамилию благодаря этому методу
        return len(self.name + self.surname)


b = User('roman', 'hero')
b.__len__()  # можно вызвать так метод
len(b)  # а можно так
