# ООП 3 Атрибуты экземпляра класса. Объектно-ориентированное программирование в Python.

class Car:
    model = 'BMW'
    engine = 1.5

a1 = Car()
a2 = Car()

a1.seat = 4  # 1. добавляем атрибут конкретному экземпляру

print(a1.__dict__)  # 2. проверяем атрибуты у экземпляра

# 3. если экземпляру класса присвоить новое значение атрибута, который есть у класса, то он перезапишется,

a1.model = 'mers'
print(a1.__dict__)

# 4. а если удалить новое значение атрибута, то вновь вернется значение атрибута класса по умолчанию

del a1.model
print(a1.__dict__)

# 5. если присвоить новый атрибут экземпляру, то он будет виден только у этого экземпляра

a1.color = 'black'
print(a1.__dict__)

# 6. если присвоить новый атрибут самому классу, то он появится у всех экземпляров

Car.size = 100
print(Car.__dict__)