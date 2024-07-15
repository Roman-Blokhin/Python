# каждая вещь имеет цену
# можно продавать вещи
# условие заполненности рюкзака
#
#

free_bagpack = 0
fool_bagpack = 2

gold = 400

sticks = 'Палки'
gas = 'Газовый баллон'

list = [sticks, gas, 'Горелка', 'Набор посуды', 'Зажигалка']
list_2 = []

# a6 = '6. Спальный мешок'
# a7 = '7. Палатка'
# a8 = '8. Фильтр для воды'
# a9 = '9. Термобелье'
# a10 = '10. Каремат'

print('\nУ тебя есть рюкзак. Сейчас он пустой, заполни его!')

while True:
    for el in range(len(list)):
        print(list[el])
    print('\n0. Заработать денег')

    answer = input('\nЧто ты выберешь: ')

    if answer == 'Палки' or answer == 'палки':
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

    elif answer == 'Газовый баллон' or answer == 'газовый баллон':
        list_2.append('Газовый баллон')
        gold -= 100
        print('Вы выбрали:', gas)

    elif answer == 'Горелка' or answer == 'горелка':
        list_2.append('Горелка')
        gold -= 100
        print('Вы выбрали:', 'Горелка')
        if gold <= 0:
            print('У вас нет денег, отправляйтесь на работу')

    elif answer == 'Набор посуды' or answer == 'набор посуды':
        list_2.append('Набор посуды')
        gold -= 100
        print('Вы выбрали:', 'Набор посуды')
        if gold <= 0:
            print('У вас нет денег, отправляйтесь на работу')

    elif answer == 'Зажигалка' or answer == 'зажигалка':
        list_2.append('Зажигалка')
        gold -= 100
        print('Вы выбрали:', 'Зажигалка')
        if gold <= 0:
            print('У вас нет денег, отправляйтесь на работу')

    elif answer == '0' or answer == 'заработать денег' or answer == 'заработать' or answer == 'Заработать денег':
        gold += 10
        print(f'Вы заработали 10 золотых, баланс: {gold} ')


    print('\nИнвентарь:', ', '.join(list_2), '\nРюкзак:', free_bagpack, '/', fool_bagpack, f'\nДеньги: {gold}')
    input('\nДля продолжения покупок нажмите Enter')

    if len(list_2) == 5:
        print('Рюкзак заполнен')
        break
