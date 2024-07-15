# каждая вещь имеет цену
# можно продавать вещи

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

# a6 = '6. Спальный мешок'
# a7 = '7. Палатка'
# a8 = '8. Фильтр для воды'
# a9 = '9. Термобелье'
# a10 = '10. Каремат'

print('\nУ тебя есть рюкзак. Сейчас он пустой, заполни его!')

while True:
    print('\n1. Магазин')
    print('2. Заработать денег')
    print('3. Проверить инвентарь')
    print('4. Продать вещи')

    answer = input('\nЧто ты выберешь: ')

    if answer == '1' or answer == 'магазин' or answer == 'Магазин':
        print('\nТовары:')
        print(' ')
        for el in range(len(list)):
            print(list[el])

        answer_1 = input('\nЧто ты выберешь: ')

        if answer_1 == 'Палки' or answer_1 == 'палки':
            if gold == 0:
                gold += 0
                print('\nУ вас нет денег, отправляйтесь на работу')
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print('\nРюкзак заполнен, продайте вещи или купите новый рюкзак')
            else:
                list_2.append(sticks)
                free_bagpack += 1
                gold -= 100
                print('Вы выбрали:', sticks)


        elif answer_1 == 'Газовый баллон' or answer_1 == 'газовый баллон':
            if gold == 0:
                gold += 0
                print('\nУ вас нет денег, отправляйтесь на работу')
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print('\nРюкзак заполнен, продайте вещи или купите новый рюкзак')
            else:
                list_2.append(gas)
                free_bagpack += 1
                gold -= 100
                print('Вы выбрали:', gas)


        elif answer_1 == 'Горелка' or answer_1 == 'горелка':
            if gold == 0:
                gold += 0
                print('\nУ вас нет денег, отправляйтесь на работу')
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print('\nРюкзак заполнен, продайте вещи или купите новый рюкзак')
            else:
                list_2.append(fire)
                free_bagpack += 1
                gold -= 100
                print('Вы выбрали:', fire)


        elif answer_1 == 'Набор посуды' or answer_1 == 'набор посуды':
            if gold == 0:
                gold += 0
                print('\nУ вас нет денег, отправляйтесь на работу')
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print('\nРюкзак заполнен, продайте вещи или купите новый рюкзак')
            else:
                list_2.append(dishes)
                free_bagpack += 1
                gold -= 100
                print('Вы выбрали:', dishes)


        elif answer_1 == 'Зажигалка' or answer_1 == 'зажигалка':
            if gold == 0:
                gold += 0
                print('\nУ вас нет денег, отправляйтесь на работу')
            elif free_bagpack == fool_bagpack:
                free_bagpack += 0
                print('\nРюкзак заполнен, продайте вещи или купите новый рюкзак')
            else:
                list_2.append(lighter)
                free_bagpack += 1
                gold -= 100
                print('Вы выбрали:', lighter)


    elif answer == '1' or answer == 'заработать денег' or answer == 'заработать' or answer == 'Заработать денег':
        gold += 10
        print(f'Вы заработали 10 золотых, баланс: {gold} ')


    print('\nИнвентарь:', ', '.join(list_2), '\nРюкзак:', free_bagpack, '/', fool_bagpack, f'\nДеньги: {gold}')
    input('\nДля продолжения нажми Enter')

    if len(list_2) == 5:
        print('Рюкзак заполнен')
        break
