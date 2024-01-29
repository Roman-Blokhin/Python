# ООП 23 Магические методы __getitem__ , __setitem__ и __delitem__. Обращение по индексу к экземпляру

class Vector:
    def __init__(self, *args):  # 1. создали метод, принимающий любое кол-во аргументов в новый список
        self.values = list(args)

    def __repr__(self):  # 2. выводим в консоль python не название экземпляра, а именно список с числами
        return str(self.values)

    # 3. в классе нельзя обратиться к элементу по индексу, поэтому нужно __getitem__
    def __getitem__(self, item):
        if 0 <= item <= len(self.values):  # 4. проверка, входит ли индекс в список значений
            return self.values[item]
        else:
            raise IndexError('Индекс за границами вселенной')  # 5. исключение, если индекс не входит

    # 6. если нам нужно по индексу заменить значение элемента, то используем __setitem__
    def __setitem__(self, key, value):  # 7. key - индекс, value: - новое значение
        if 0 <= key <= len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами вселенной')

    # 7. если нам нужно удалить значение элемента по индексу, то используем __delitem__
    def __delitem__(self, item):
        if 0 <= item <= len(self.values):
            del (self.values[item])
        else:
            raise IndexError('Индекс за границами вселенной')
