# ООП 12 Property Вычисляемые свойства (Calculated properties python)

class Square:
    def __init__(self, side):
        self.side = side

    @property  # делаем из метода свойство, чтобы мы вызывали его ни как метод, а как атрибут - a.area
    def area(self):
        return self.side**2