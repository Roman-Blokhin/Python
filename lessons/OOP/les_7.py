# ООП 7 Практика "Создание класса и его методов". Объектно-ориентированное программирование в Python.

from math import sqrt


class Point:
    list_points = []  # список, куда будут добавляться все точки, к которым можно обращаться по индексу

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)  # добавляем каждый новый атрибут в список

    def move_to(self, new_x, new_y):  # метод будет менять значение точки
        self.x = new_x
        self.y = new_y

    def go_home(self):  # возвращает к нулевым координатам
        self.move_to(0, 0)  # мы заменили замену координат, прописав метод внутри метода

    def print_point(self):  # красиво выводит наши координаты
        print(f'Точка {self}, с координатами ({self.x}, {self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):  # проверяем, принадлежит ли точка к классу Point
            raise ValueError('Точка не принадлежит к классу POINT')  # исключение, если точка не принадлежит классу

        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)  # разница точек по Пифагору

p1 = Point(3, 4)
p2 = Point(-23, 84)
p3 = Point()
print(p3.x, p3.y)

p3.move_to(4, -90)
print(p3.x, p3.y)

p1.go_home()
print(p1.x, p1.y)

