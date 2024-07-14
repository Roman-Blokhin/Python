from variables import *
from menu import *
from gold_work import *


def gold_worker():
    gold += 100
    print('\nЗолото:', gold,
          '     Дерево:', wood,
          '     Люди:', people_1, '/', people_2,
          '     Свободные люди: ', free_people)


while True:
    print('\nПривет, это игра про ремесло! Поехали:  ')
    print (menu_1)  # продолжить
    print (menu_2)  # выход
    click_1 = input('Выберите действие: ')
    if click_1 == '1':
        print('\nЗолото:', gold,
              '     Дерево:', wood,
              '     Люди:', people_1, '/', people_2,
              '     Свободные люди: ', free_people)

        print ('\n' + menu_3)  # добыть золото
        print (menu_4)  # добыть дерево
        print (menu_5)  # построить
        print (menu_2)  # выход
        click_2 = input('Выберите действие: ')

        if click_2 == '1':
            free_people -= 1
            gold += 100
            print('\nЗолото:', gold,
                  '     Дерево:', wood,
                  '     Люди:', people_1, '/', people_2,
                  '     Свободные люди: ', free_people)

            print(menu_6)  # добыть
            print(menu_7)  # закончить добывать
            print(menu_2)  # выход
            click_3 = input('Выберите действие: ')
            if click_3 == '1':
                gold_worker()
            if click_3 == '2':
                print('Игра окончена..')
            if click_3 == '0':
                print('Игра окончена..')
                break


    elif first_click == '2':
        print('Игра окончена..')
        break
