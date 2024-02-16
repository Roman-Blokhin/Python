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
        # 5. при изменении значения, оно меняется через сеттер

# --------------------------------------------------------------
# Наследование

# 1. если мы наследуем, то у дочернего класса есть атрибут __dict__, и мы можем создавать новые атрибуты
class Square(Rect_2):
    pass

a = Square(4, 90)
print(a.width, a.height)
a.color = 'red'  # 2. можем создавать новые атрибуты
print(a.width, a.height, a.color)


# --------------------------------------------------------------

# 1. если мы хотим ограничить создание атрибутов, то мы обращаемся к __slots__ у родительского класса
class Sql(Rect_2):
    __slots__ = 'color'  # 2. мы не просто задаем 1 атрибут, мы расширяем родительский __slots__
    def __init__(self, a, b, color):
        super().__init__(a, b)  # 3. забираем описание __init__ у родительского класса
        self.color = color  # 4. добавляем новый атрибут color в инициализацию (__init__)

b = Sql(4, 6, 'red')
print(b.color, b.width, b.height)
# атрибут __dict__ м не можем теперь вызвать, потому что у нас есть __slots__ - ограничение по кол-ву атрибутов

# --------------------------------------------------------------

class Sql_2(Rect_2):
    __slots__ = tuple()  # 1. если мы не хотим расширять __slots__, просто задаем пустой кортеж
    def __init__(self, a, b):
        super().__init__(a, b)

c = Sql_2(1, 2)
print(c.width, c.height)
# print(c.__dict__)  # 2. так как есть __slots__, атрибута __dict__ у нас нет
