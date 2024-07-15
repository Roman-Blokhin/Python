free_bagpack = 0
fool_bagpack = 5

list = ['Палки', 'Газовый баллон', 'Горелка', 'Набор посуды', 'Зажигалка']
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

    answer = input('\nЧто ты выберешь: ')

    if answer == 'Палки' or answer == 'палки':
        list_2.append('Палки')
        print('Вы выбрали:', 'Палки')

    elif answer == 'Газовый баллон' or answer == 'газовый баллон':
        list_2.append('Газовый баллон')
        print('Вы выбрали:', 'Газовый баллон')

    elif answer == 'Горелка' or answer == 'горелка':
        list_2.append('Горелка')
        print('Вы выбрали:', 'Горелка')

    elif answer == 'Набор посуды' or answer == 'набор посуды':
        list_2.append('Набор посуды')
        print('Вы выбрали:', 'Набор посуды')

    elif answer == 'Зажигалка' or answer == 'зажигалка':
        list_2.append('Зажигалка')
        print('Вы выбрали:', 'Зажигалка')

    print('\nВ вашем рюкзаке теперь:', ', '.join(list_2))
    print('\nВместимость рюкзака:', str(len(list_2)) + '/5')
    input('\nДля продолжения покупок нажмите Enter')

    if len(list_2) == 5:
        print('Рюкзак заполнен')
        break
