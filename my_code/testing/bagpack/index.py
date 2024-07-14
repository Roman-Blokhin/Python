free_bagpack = 0
fool_bagpack = 5

list = ['1. Палки', '2. Газовый баллон', '3. Горелка', '4. Набор посуды', '5. Зажигалка']
list_2 = []

# a6 = '6. Спальный мешок'
# a7 = '7. Палатка'
# a8 = '8. Фильтр для воды'
# a9 = '9. Термобелье'
# a10 = '10. Каремат'

print('У тебя есть рюкзак. Сейчас он пустой, заполни его!')

while True:
    for el in range(len(list)):
        print(list[el])

    answer = input('Что ты выберешь? ')

    if answer == '1':
        a1 = list.pop(0)
        list_2.append(a1)
        print('Вы выбрали:', a1)
        print('В вашем рюкзаке теперь: ')
        for x in range(len(list_2)):
            print(list_2)
        input()
