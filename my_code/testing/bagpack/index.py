from colorama import Fore, Back, Style

free_bagpack = 0
fool_bagpack = 2

gold = 400

sticks = 'Палки'
gas = 'Газовый баллон'
fire = 'Горелка'
dishes = 'Набор посуды'
lighter = 'Зажигалка'

list = [sticks, gas, fire, dishes, lighter]
list_2 = []

print(Fore.RED + '\nУ тебя есть рюкзак. Сейчас он пустой, заполни его!' + Style.RESET_ALL)

while True:
    print('\n1. Магазин')
    print('2. Заработать денег')
    print('3. Проверить инвентарь')
    print('4. Продать вещи')

    answer = input(Fore.GREEN + '\nЧто ты выберешь: ' + Style.RESET_ALL)

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
                gold -= 100
                print('Вы выбрали:', Fore.RED + sticks + Style.RESET_ALL)


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
                gold -= 100
                print('Вы выбрали:', Fore.RED + gas + Style.RESET_ALL)


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
                gold -= 100
                print('Вы выбрали:', Fore.RED + fire + Style.RESET_ALL)


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
                gold -= 100
                print('Вы выбрали:', Fore.RED + dishes + Style.RESET_ALL)


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
                gold -= 100
                print('Вы выбрали:', Fore.RED + lighter + Style.RESET_ALL)


    elif answer == '1' or answer == 'заработать денег' or answer == 'заработать' or answer == 'Заработать денег':
        gold += 10
        print(Fore.RED + f'Вы заработали 10 золотых, баланс: {gold} ' + Style.RESET_ALL)


    print('\nИнвентарь:', Fore.YELLOW + ', '.join(list_2) + Style.RESET_ALL,
          '\nРюкзак:', free_bagpack, '/', fool_bagpack,
          f'\nДеньги: {gold}')
    input(Fore.BLUE + '\nДля продолжения нажми Enter ' + Style.RESET_ALL)

    if len(list_2) == 5:
        print(Fore.RED + 'Рюкзак заполнен' + Style.RESET_ALL)
        break

# --------------------------------------

# каждая вещь имеет цену
# можно продавать вещи