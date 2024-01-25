# ООП 19 Магические методы __eq__ и __hash__. Dunder methods в Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # когда мы прописываем метод __eq__, мы не можем вызвать метод __hash__ от id
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    # хеш нельзя найти у изменяемых объектов - списки
    # хеширование используется в словарях

    # так как от id мы не можем хешировать, нам нужно определить, от чего произведется хеш
    def __hash__(self):
        return hash((self.x, self.y))

    # у одинаковых объектов: a = Point(1, 2) и b = Point(1, 2) - хеш будет одинаковый