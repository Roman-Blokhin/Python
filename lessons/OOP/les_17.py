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


class Otrezok:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __len__(self):  # 3. автоматически подтягивает встроенную функцию, когда прописан сам метод в классе
        return abs(self)  # self.__abs__()

    def __abs__(self):  # 2. прописываем метод, который убирает минус у числа
        return abs(self.x2 - self.x1)

q = Otrezok(90, 6)
len(q)  # выводит положительное число