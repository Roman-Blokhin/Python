from colorama import Fore, Back, Style

# ----------------------------------------------- ПЕРЕМЕННЫЕ -----------------------------------------------

free_bagpack = 0
fool_bagpack = 5

gold = 400

sticks = 'Палки'
gas = 'Газовый баллон'
fire = 'Горелка'
dishes = 'Набор посуды'
lighter = 'Зажигалка'

sticks_cost = 80
gas_cost = 50
fire_cost = 120
dishes_cost = 100
lighter_cost = 30

list = [sticks, gas, fire, dishes, lighter]
list_2 = []

# ----------------------------------------------- ФУНКЦИИ -----------------------------------------------

def inventory():
    print('\nИнвентарь:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL,
          '\nРюкзак:', free_bagpack, '/', fool_bagpack,
          f'\nДеньги: {gold}')
    input(Fore.BLUE + '\nДля продолжения нажми Enter ' + Style.RESET_ALL)

# ----------------------------------------------- ПРЕДИСЛОВИЕ -----------------------------------------------

print(Fore.RED + '\nУ тебя есть рюкзак. Сейчас он пустой, заполни его!' + Style.RESET_ALL)

while True:
# ----------------------------------------------- ГЛАВНОЕ МЕНЮ -----------------------------------------------

    print('\n1. Магазин')
    print('2. Заработать денег')
    print('3. Проверить инвентарь')
    print('4. Продать вещи')

    answer = input(Fore.GREEN + '\nЧто ты выберешь: ' + Style.RESET_ALL)

# ----------------------------------------------- МЕНЮ - МАГАЗИН -----------------------------------------------

    if answer == '1' or answer == 'магазин' or answer == 'Магазин':
        print(Fore.RED + '\nТовары:' + Style.RESET_ALL)
        print(' ')
        for el in range(len(list)):
            print(list[el])

        answer_1 = input(Fore.GREEN + '\nЧто ты выберешь: ' + Style.RESET_ALL)

        if answer_1 == 'Палки' or answer_1 == 'палки':
            if gold == 0:
                gold += 0
                print(Fore.RED + '\nУ вас нет денег, отправляйтесь на работу' + Style.RESET_ALL)
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print(Fore.RED + '\nРюкзак заполнен, продайте вещи или купите новый рюкзак' + Style.RESET_ALL)
            else:
                list_2.append(sticks)
                free_bagpack += 1
                gold -= sticks_cost
                print('Вы выбрали:', Fore.RED + sticks + Style.RESET_ALL)
                inventory()


        elif answer_1 == 'Газовый баллон' or answer_1 == 'газовый баллон':
            if gold == 0:
                gold += 0
                print(Fore.RED + '\nУ вас нет денег, отправляйтесь на работу' + Style.RESET_ALL)
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print(Fore.RED + '\nРюкзак заполнен, продайте вещи или купите новый рюкзак' + Style.RESET_ALL)
            else:
                list_2.append(gas)
                free_bagpack += 1
                gold -= gas_cost
                print('Вы выбрали:', Fore.RED + gas + Style.RESET_ALL)
                inventory()


        elif answer_1 == 'Горелка' or answer_1 == 'горелка':
            if gold == 0:
                gold += 0
                print(Fore.RED + '\nУ вас нет денег, отправляйтесь на работу' + Style.RESET_ALL)
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print(Fore.RED + '\nРюкзак заполнен, продайте вещи или купите новый рюкзак' + Style.RESET_ALL)
            else:
                list_2.append(fire)
                free_bagpack += 1
                gold -= fire_cost
                print('Вы выбрали:', Fore.RED + fire + Style.RESET_ALL)
                inventory()


        elif answer_1 == 'Набор посуды' or answer_1 == 'набор посуды':
            if gold == 0:
                gold += 0
                print(Fore.RED + '\nУ вас нет денег, отправляйтесь на работу' + Style.RESET_ALL)
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print(Fore.RED + '\nРюкзак заполнен, продайте вещи или купите новый рюкзак' + Style.RESET_ALL)
            else:
                list_2.append(dishes)
                free_bagpack += 1
                gold -= dishes_cost
                print('Вы выбрали:', Fore.RED + dishes + Style.RESET_ALL)
                inventory()


        elif answer_1 == 'Зажигалка' or answer_1 == 'зажигалка':
            if gold == 0:
                gold += 0
                print(Fore.RED + '\nУ вас нет денег, отправляйтесь на работу' + Style.RESET_ALL)
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print(Fore.RED + '\nРюкзак заполнен, продайте вещи или купите новый рюкзак' + Style.RESET_ALL)
            else:
                list_2.append(lighter)
                free_bagpack += 1
                gold -= lighter_cost
                print('Вы выбрали:', Fore.RED + lighter + Style.RESET_ALL)
                inventory()

# --------------------------------------- МЕНЮ - ЗАРАБОТАТЬ ДЕНЕГ ---------------------------------------

    elif answer == '2' or answer == 'заработать денег' or answer == 'заработать' or answer == 'Заработать денег':
        gold += 10
        print(Fore.RED + '\n' + f'Вы заработали 10 золотых, баланс: {gold} ' + Style.RESET_ALL)

# --------------------------------------- МЕНЮ - ПРОВЕРИТЬ ИНВЕНТАРЬ ---------------------------------------

    elif answer == '3' or answer == 'инвентарь' or answer == 'проверить инвентарь' or answer == 'проверить инвентарь':
        inventory()

# --------------------------------------- МЕНЮ - ПРОДАТЬ ВЕЩИ ---------------------------------------

    elif answer == '4' or answer == 'продать вещи' or answer == 'продать' or answer == 'Продать вещи':
        if free_bagpack == 0:
            print('\nВаш рюкзак пуст')
            input(Fore.BLUE + '\nДля продолжения нажми Enter ' + Style.RESET_ALL)
        else:
            print('\nИнвентарь:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL)
            answer_2 = input('Что вы хотите продать? ')

            if answer_2 == 'Палки' or answer_2 == 'палки':
                gold += sticks_cost
                free_bagpack -= 1
                list_2.remove(sticks)
                print(f'Вы продали {sticks}')
                print('В вашем рюкзаке:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL)

            if answer_2 == 'Газовый баллон' or answer_2 == 'газовый баллон':
                gold += gas_cost
                free_bagpack -= 1
                list_2.remove(gas)
                print(f'Вы продали {gas}')
                print('В вашем рюкзаке:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL)

            if answer_2 == 'Горелка' or answer_2 == 'горелка':
                gold += fire_cost
                free_bagpack -= 1
                list_2.remove(fire)
                print(f'Вы продали {fire}')
                print('В вашем рюкзаке:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL)

            if answer_2 == 'Набор посуды' or answer_2 == 'набор посуды':
                gold += dishes_cost
                free_bagpack -= 1
                list_2.remove(dishes)
                print(f'Вы продали {dishes}')
                print('В вашем рюкзаке:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL)

            if answer_2 == 'Зажигалка' or answer_2 == 'зажигалка':
                gold += lighter_cost
                free_bagpack -= 1
                list_2.remove(lighter)
                print(f'Вы продали {lighter}')
                print('В вашем рюкзаке:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL)


# --------------------------------------- МЕНЮ - ПРОДАТЬ ВЕЩИ ---------------------------------------

    if len(list_2) == 5:
        print(Fore.RED + 'Рюкзак заполнен' + Style.RESET_ALL)
        break

# --------------------------------------

# каждая вещь имеет цену
# можно продавать вещи