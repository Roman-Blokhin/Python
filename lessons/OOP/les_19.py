# ООП 18 Специальные методы сравнения объектов классов

# __eq__ - отвечает за ==
# __ne__ - отвечает за !=
# __lt__ - отвечает за <
# __le__ - отвечает за <=
# __gt__ - отвечает за >
# __ge__ - отвечает за >=

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rect):
            return self.a == other.a and self.b == other.b
        raise AttributeError(f'Новое значение: {other} не принадлежит к классу Rect')

    def __ne__(self, other):
        return self.a != other.a and self.b != other.b

    def __lt__(self, other):  # позволяет не прописывать оборотные методы сравнения
        if isinstance(other, Rect):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if isinstance(other, Rect):
            return self.area > other.area
        if isinstance(other, (int, float)):
            return self.area > other

    def __ge__(self, other):
        if isinstance(other, Rect):
            return self.area >= other.area
        if isinstance(other, (int, float)):
            return self.area >= other


# Можно реализовать только методы: __eq__ , __lt__ , __le__ - все остальные считаются обратной стороной,
# поэтому в любом случае будут вызваны по логике питона