# ООП 33 Slots свойства и наследование в Python. Slots Property Inheritance

class Rect:

    __slots__ = ('width', 'height')  # 1. основные атрибуты класса

    def __init__(self, a, b):
        self.width = a
        self.height = b

    # 2. свойства мы можем навесить и вызывать их как атрибуты у элементов, не изменяя их
    @property
    def perimetr(self):
        return (self.width + self.height)*2

    @property
    def area(self):
        return self.width * self.height