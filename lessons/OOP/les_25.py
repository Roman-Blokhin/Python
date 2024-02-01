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
        self.index = 0  # 4. обозначение начала индекса
        return self

    # 3. делаем итерацию по символам у нашего элемента surname
    def __next__(self):
        if self.index >= len(self.name):  # 8. чтобы не было ошибок и итерация заканчивалась на посл. символе
            raise StopIteration
        letter = self.name[self.index]  # 5. чтобы итерация начиналась с первого символа
        self.index += 1  # 6. смещаем индекс вправо, прибавляя + 1 до окончания количества символов
        return letter  # 7. возвращаем с первого символа и до конца

person = User('Roman', 'Ivanov', [1, 2, 44, 3, 4])
for i in person:
    print (i)

