# ООП 24 Магические методы __iter__ и __next__ Итерация экземпляров класса Python

class User:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    # 1. наша задача провести итерацию элемента
    def __getitem__(self, item):  # 2. неофициальный и не приоритетный способ, если есть __iter__
        return self.marks[item]

    # 2. если есть __iter__, то __getitem__ игнорируется
    def __iter__(self):
        return iter(self.surname)

person = User('Roman', 'Ivanov', [1, 2, 44, 3, 4])
for i in person:
    print (i)

