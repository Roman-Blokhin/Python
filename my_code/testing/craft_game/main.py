from variables import *
from menu import *

while True:
    print('\nПривет, это игра про ремесло! Поехали:  ')
    print (menu_1)
    print (menu_2)
    first_click = input('Выберите действие: ')
    if first_click == '1':
        print('Золото:', gold, '     Дерево:', wood, '     Люди:', people_1, '/', people_2)
        input()
    elif first_click == '2':
        print('Игра окончена..')
        break
