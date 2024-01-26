# ООП 20 Магический метод __bool__ Правдивость объектов в Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 3. bool определяет False или True с помощью вычислений, если цифры. Если результат 0 = False, остальное True
    def __len__(self):
        return abs(self.x - self.y)

    # 4. прописываем условие, для определения булевого значения, чтобы оно всегда было True, кроме: s = Point(0, 0)
    def __bool__(self):
        return self.x != 0 or self.y !=0

a = Point(1, 2)
b = Point(2, 2)

print(bool(a))  # 3.1 разница координат != 0
print(bool(b))  # 3.2 разница координат == 0





# 1. Числа: 0 = False, все остальные = True
# 2. Коллекции(списки, строки, кортежи и т.д.): пустые = False, если есть хоть 1 символ = True