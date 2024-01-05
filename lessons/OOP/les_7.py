# ООП 7 Практика "Создание класса и его методов". Объектно-ориентированное программирование в Python.

class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y

    def move_to(self, new_x, new_y):  # метод будет менять значение точки
        self.x = new_x
        self.y = new_y

    def go_home(self):  # возвращает к нулевым координатам
        self.x = 0
        self.y = 0

p1 = Point(3, 4)
p2 = Point(-23, 84)
p3 = Point()
print(p3.x, p3.y)

p3.move_to(4, -90)
print(p3.x, p3.y)

p1.go_home()
print(p1.x, p1.y)
