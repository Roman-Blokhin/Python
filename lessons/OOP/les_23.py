# ООП 21 Магический метод __call__ Делаем экземпляры вызываемыми. Callable instance Python

class Counter:
    def __init__(self):
        self.count = 0
        print(f'New object: {self}')

    def __call__(self, *args, **kwargs):
        self.count += 1
        return f'Счетчик вызван {self.count} раз'