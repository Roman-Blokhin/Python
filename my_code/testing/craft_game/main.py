from variables import *
from menu import *
# from gold_work import gold_worker
from resources import res


def gold_worker():
    while True:
        global gold
        print('\nЗолото:', gold, '     Дерево:', wood, '     Люди:', people_1, '/', people_2,
              '     Свободные люди: ', free_people)
        print(menu_6)
        print(menu_0)
        click_3_1 = input()
        if click_3_1 == '1':
            gold += 100
        elif click_3_1 == '0':
            break

while True:
    # -----------------------------------  НАЧАЛЬНО МЕНЮ  -----------------------------------
    print('\nПривет, это игра про ремесло! Поехали:  ')
    print (menu_1)  # продолжить
    print (menu_2)  # выход
    click_1 = input('Выберите действие: ')

    # -----------------------------------  ГЛАВНОЕ МЕНЮ  -----------------------------------
    if click_1 == '1':
        print(res)

        print ('\n' + menu_3)  # добыть золото
        print (menu_4)  # добыть дерево
        print (menu_5)  # построить
        print (menu_2)  # выход
        click_2 = input('Выберите действие: ')

        if click_2 == '1':
            free_people -= 1
            gold_worker()

            free_people += 1
            print(res)
            print(menu_6)  # добыть
            print(menu_7)  # закончить добывать
            print(menu_2)  # выход

            # -----------------------------------  МЕНЮ ДОБЫЧИ ЗОЛОТА  -----------------------------------
            click_3 = input('Выберите действие: ')
            if click_3 == '1':
                gold_worker()

            # -----------------------------------  МЕНЮ   -----------------------------------
            elif click_3 == '2':
                print('Hello craft game')
            elif click_3 == '0':
                print('Игра окончена..')
                break


    elif first_click == '2':
        print('Игра окончена..')
        break