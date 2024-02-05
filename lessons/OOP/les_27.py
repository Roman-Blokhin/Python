# ООП 26 Наследование от object и от других встроенных типов. object parent class Python

class Person:
    pass


class Doctor(Person):
    pass

a = object
print(a)


# У родительского класса есть класс object, у которого он наследует магические методы
# класс object не прописывается, но он фактически является прародителем всех классов,
# а в python все является объектами

# есть также встроенные классы: list, dict, int, str и другие, у них тоже есть свои встроенные функции,
# но над ними все равно стоит класс object

class Mylist(list):
    pass

b = Mylist()
print(b)  # выдает пустой список
b.append(56)  # используем встроенную функцию списков - добавление в конец списка
b.append('dfhdhdf')
print(b)
