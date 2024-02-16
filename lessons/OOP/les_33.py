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


# --------------------------------------------------------------
# Мы можем сделать из свойств геттеры и сеттеры, чтобы изменять значения атрибутов

class Rect_2:

    __slots__ = ('__width', 'height')  # 1. делаем один атрибут защищенным

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property  # геттер
    def width(self):  # 2. меняем название метода
        return self.__width

    @width.setter  # 3. прописываем свойство сеттера по названию геттера
    def width(self, value):  # 4. меняем название метода, относительно названия свойства геттера
        print('setter called')
        self.__width = value
        # при изменения значения, оно меняется через сеттер