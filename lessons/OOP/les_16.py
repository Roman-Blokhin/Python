# ООП 15 Магические методы. Методы __str__ и __repr__. (Dunder methods)

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # 1. отвечает за то, как отображается объект в системе, для разработчиков
        return f"Lion - {self.name}"

    def __str__(self):  # 2. отвечает за то, как отображается объект для пользователя
        return f"Lion name is {self.name}"
