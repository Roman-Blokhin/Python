# ООП 2 Атрибуты класса. Объектно-ориентированное программирование в Python

class Person:
    name = 'Ivan'
    age = 30

print(Person)
print(Person.__dict__)  # 1. посмотреть все атрибуты класса

print(getattr(Person, 'name'))  # 2. можно вызвать определенный атрибут
print(getattr(Person, 'x', 600))  # 3. если атрибута нет, то 3им параметром передаем значение, которое нужно вывести

Person.name = 'Roman'  # 4. меняем значение атрибута
print(Person.name)

Person.toy = 'fish'  # 5. мы автоматически создаем новый атрибут и присваиваем ему значение

setattr(Person, 'y', 'semen')  # 6. можно создать новый атрибут класса
print(Person.y)

setattr(Person, 'toy', 555)  # 7. можно изменять уже существующие атрибуты
print(Person.toy)

print(Person.__dict__)

del Person.y  # 8. удаление атрибута, 1 способ
print(Person.__dict__)

delattr(Person, 'toy')  # 9. удаление атрибута, 2 способ
print(Person.__dict__)

# 10. если удалить атрибут у класса, то он удалится у всех экземпляров класса

class Car:
    model = 'Mers'
    engine = 1.5

a = Car()
b = Car()

del Car.model

# 11. если добавить атрибут к конкретному экземпляру класса, то он появится только у него

a.color = 'green'

print(a.color)