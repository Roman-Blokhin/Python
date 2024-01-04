# ООП 5 Методы экземпляра. Аргумент self. Объектно-ориентированное программирование в Python.

class Cat:
    breed = 'pers'

    def hello(self):
        print('Hello world')

    def show_breed(self):
        print(f'Порода у нашей кошки: {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):  # hasattr - проверяет, есть ли атрибут у экземпляра
            print(f'Имя у нашей кошки: {self.name}')
        else:
            print(f'У нашей кошки нет имени')

    def set_value(self, value, age=0):  # говорим функции, что будет передано значение - value и возраст 0(по умолчанию)
        self.name = value  # автоматически создаем атрибут - name, которому сразу присваиваем переданное значение
        self.age = age


bob = Cat()
jim = Cat()

# 1. можно обратиться к функции через класс
print('1')
Cat.show_breed(bob)

# 2. можно обратиться к функции(методу) напрямую через экземпляр
print('2')
bob.show_breed()

# 3. можно поменять значение аргумента
bob.breed = 'whiter'
print('3')
bob.show_breed()

# 4. проверим, есть ли имя у кошки (должен быть присвоен новый атрибут экземпляру
bob.name = 'BOB'  # присвоили новый атрибут к экземпляру - bob
print('4')
bob.show_name()
jim.show_name()  # у кошки - jim, нет имени

# 5. передаем в функцию значение, которое присваиваем только что созданному атрибуту - name у нашего экземпляра
bob.set_value('BOB')
print('5')
bob.show_name()

# 6. если мы не передаем второе значение в функции - set_value(), то оно по умолчанию будет - 0
print('6')
bob.set_value('bob')  # возраст будет по умолчанию - 0, потому что не передали новое значение
print(bob.age)
bob.set_value('Boby', 15)  # передали значение, поэтому возраст будет - 15
print(bob.age)
