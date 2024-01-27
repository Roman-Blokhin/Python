# ООП 22 Полиморфизм в Python. Polymorphism python
# Полиморфизм - возможность обработки разных объектов одним методом по одному названию
# Смысл в том, чтобы у всех методов В РАЗНЫХ КЛАССАХ было одно название
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangle {self.a}x{self.b} ='

class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2

    def __str__(self):
        return f'Square {self.a}x{self.a} ='

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2

    def __str__(self):
        return f'Circle radius {self.r} ='

rect1 = Rect(3, 4)
rect2 = Rect(30, 40)

# print(rect1.get_rect_area(), rect2.get_rect_area())

sq1 = Square(3)
sq2 = Square(30)

# print(sq1.get_square_area(), sq2.get_square_area())

cir1 = Circle(2)
cir2 = Circle(70)

# print(sq1.get_square_area(), sq2.get_square_area())

figures = [rect1, rect2, sq1, sq2, cir1, cir2]

# первый неудобный метод:
for i in figures:
    if isinstance(i, Rect):
        print(i.get_area())
    elif isinstance(i, Square):
        print(i.get_area())
    elif isinstance(i, Circle):
        print(i.get_area())

print('')

# второй удобный метод:
for i in figures:
    print(i, i.get_area())