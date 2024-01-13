# ООП 12 Property Вычисляемые свойства (Calculated properties python)

class Square:
    def __init__(self, side):
        self.side = side
        self.__area = None  # 2. создали приватную переменную для определения площади. По умолчанию = None

    @property  # 1. делаем из метода свойство, чтобы мы вызывали его ни как метод, а как атрибут - a.area
    def area(self):
        if self.__area is None:  # 3. проверка, если переменная пустая, то в нее записывается 1 раз значение площади
            print('create area')
            self.__area = self.side**2
        return self.__area