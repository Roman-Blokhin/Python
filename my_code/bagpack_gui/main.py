from tkinter import *
from tkinter import ttk
from vars import *


# --------------------------------------- ФУНКЦИИ - МАГАЗИН ---------------------------------------

def stick_btn():  # кнопка - ПАЛКИ
    global gold, list_inventory, min_bag, max_bag
    if gold < sticks_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= sticks_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(sticks)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_11.config(state='normal')
            lbl_34.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def gas_btn():  # кнопка - ГАЗ
    global gold, list_inventory, min_bag, max_bag
    if gold < gas_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= gas_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(gas)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_12.config(state='normal')
            lbl_35.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def lighter_btn():  # кнопка - ЗАЖИГАЛКА
    global gold, list_inventory, min_bag, max_bag
    if gold < lighter_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= lighter_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(lighter)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_13.config(state='normal')
            lbl_36.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def karemat_btn():  # кнопка - КАРЕМАТ
    global gold, list_inventory, min_bag, max_bag
    if gold < karemat_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= karemat_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(karemat)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_14.config(state='normal')
            lbl_37.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def fire_btn():  # кнопка - ГОРЕЛКА
    global gold, list_inventory, min_bag, max_bag
    if gold < fire_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= fire_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(fire)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_15.config(state='normal')
            lbl_38.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def dishes_btn():  # кнопка - ПОСУДА
    global gold, list_inventory, min_bag, max_bag
    if gold < dishes_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= dishes_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(dishes)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_16.config(state='normal')
            lbl_39.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def sleeping_bag_btn():  # кнопка - СПАЛЬНИК
    global gold, list_inventory, min_bag, max_bag
    if gold < sleeping_bag_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= sleeping_bag_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(sleeping_bag)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_17.config(state='normal')
            lbl_40.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def flashlight_btn():  # кнопка - ФОНАРЬ
    global gold, list_inventory, min_bag, max_bag
    if gold < flashlight_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= flashlight_cost
            lbl_11.config(text=gold)
            lbl_19.config(text=gold)
            lbl_26.config(text=gold)
            lbl_46.config(text=gold)
            print('\nДеньги:', gold)
            list_inventory.append(flashlight)
            lbl_14.config(text=list_inventory)
            lbl_29.config(text=list_inventory)
            lbl_52.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            lbl_27.config(text=(min_bag, '/', max_bag))
            lbl_48.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
            btn_18.config(state='normal')
            lbl_41.config(fg='red')
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=14, column=0, columnspan=4)
            print(full_bag)


def level_up():  # кнопка - ПОВЫСИТЬ УРОВЕНЬ РЮКЗАКА
    global gold, level, max_bag
    if gold >= level_bagpack_cost:
        gold -= level_bagpack_cost
        level += 1
        lbl_11.config(text=gold)
        lbl_19.config(text=gold)
        lbl_26.config(text=gold)
        lbl_46.config(text=gold)
        print('\nДеньги:', gold)
        lbl_13.config(text=level)
        lbl_28.config(text=level)
        lbl_50.config(text=level)
        print('Уровень:', level)
        lbl_12.config(text=(min_bag, '/', max_bag + 5))
        lbl_27.config(text=(min_bag, '/', max_bag + 5))
        lbl_48.config(text=(min_bag, '/', max_bag + 5))
        max_bag += 5
        btn_19.config(state='normal')
        lbl_42.config(fg='red')
    else:
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=13, column=0, columnspan=4)
        gold -= 0
        level += 0


# --------------------------------------- ФУНКЦИИ - МАГАЗИН ---------------------------------------

def work():
    global gold
    gold += 1
    lbl_19.config(text=gold)
    lbl_11.config(text=gold)
    lbl_26.config(text=gold)
    lbl_46.config(text=gold)
    print('Деньги:', gold)


# --------------------------------------- ФУНКЦИИ - ПРОДАЖА ---------------------------------------

def sell_stick_btn():  # кнопка - ПРОДАТЬ ПАЛКИ
    global gold, list_inventory, min_bag, max_bag
    gold += sticks_cost_sell
    lbl_11.config(text=gold)
    lbl_19.config(text=gold)
    lbl_26.config(text=gold)
    lbl_46.config(text=gold)
    print('\nДеньги:', gold)
    list_inventory.remove(sticks)
    lbl_14.config(text=list_inventory)
    lbl_29.config(text=list_inventory)
    lbl_52.config(text=list_inventory)
    print('Инвентарь:', list_inventory)
    min_bag -= 1
    lbl_12.config(text=(min_bag, '/', max_bag))
    lbl_27.config(text=(min_bag, '/', max_bag))
    lbl_48.config(text=(min_bag, '/', max_bag))
    print('Товаров в рюкзаке:', min_bag, '/', max_bag)
    if sticks not in list_inventory:
        btn_11.config(state='disabled')
        lbl_34.config(fg='grey')
        lbl_52.config(text='Пусто')
        print('\nПродано:', sticks)

def sell_gas_btn():  # кнопка - ПРОДАТЬ ГАЗ
    global gold, list_inventory, min_bag, max_bag
    gold += gas_cost_sell
    lbl_11.config(text=gold)
    lbl_19.config(text=gold)
    lbl_26.config(text=gold)
    lbl_46.config(text=gold)
    print('\nДеньги:', gold)
    list_inventory.remove(gas)
    lbl_14.config(text=list_inventory)
    lbl_29.config(text=list_inventory)
    lbl_52.config(text=list_inventory)
    print('Инвентарь:', list_inventory)
    min_bag -= 1
    lbl_12.config(text=(min_bag, '/', max_bag))
    lbl_27.config(text=(min_bag, '/', max_bag))
    lbl_48.config(text=(min_bag, '/', max_bag))
    print('Товаров в рюкзаке:', min_bag, '/', max_bag)
    if gas not in list_inventory:
        btn_12.config(state='disabled')
        lbl_35.config(fg='grey')
        lbl_52.config(text='Пусто')
        print('\nПродано:', gas)


def sell_lighter_btn():  # кнопка - ПРОДАТЬ ЗАЖИГАЛКУ
    global gold, list_inventory, min_bag, max_bag
    gold += lighter_cost_sell
    lbl_11.config(text=gold)
    lbl_19.config(text=gold)
    lbl_26.config(text=gold)
    lbl_46.config(text=gold)
    print('\nДеньги:', gold)
    list_inventory.remove(lighter)
    lbl_14.config(text=list_inventory)
    lbl_29.config(text=list_inventory)
    lbl_52.config(text=list_inventory)
    print('Инвентарь:', list_inventory)
    min_bag -= 1
    lbl_12.config(text=(min_bag, '/', max_bag))
    lbl_27.config(text=(min_bag, '/', max_bag))
    lbl_48.config(text=(min_bag, '/', max_bag))
    print('Товаров в рюкзаке:', min_bag, '/', max_bag)
    if lighter not in list_inventory:
        btn_13.config(state='disabled')
        lbl_36.config(fg='grey')
        lbl_52.config(text='Пусто')
        print('\nПродано:', lighter)


def sell_karemat_btn():  # кнопка - ПРОДАТЬ КАРЕМАТ
    global gold, list_inventory, min_bag, max_bag
    gold += karemat_cost_sell
    lbl_11.config(text=gold)
    lbl_19.config(text=gold)
    lbl_26.config(text=gold)
    lbl_46.config(text=gold)
    print('\nДеньги:', gold)
    list_inventory.remove(karemat)
    lbl_14.config(text=list_inventory)
    lbl_29.config(text=list_inventory)
    lbl_52.config(text=list_inventory)
    print('Инвентарь:', list_inventory)
    min_bag -= 1
    lbl_12.config(text=(min_bag, '/', max_bag))
    lbl_27.config(text=(min_bag, '/', max_bag))
    lbl_48.config(text=(min_bag, '/', max_bag))
    print('Товаров в рюкзаке:', min_bag, '/', max_bag)
    if karemat not in list_inventory:
        btn_14.config(state='disabled')
        lbl_37.config(fg='grey')
        lbl_52.config(text='Пусто')
        print('\nПродано:', karemat)


def sell_fire_btn():  # кнопка - ПРОДАТЬ ГОРЕЛКА
    global gold, list_inventory, min_bag, max_bag
    gold += fire_cost_sell
    lbl_11.config(text=gold)
    lbl_19.config(text=gold)
    lbl_26.config(text=gold)
    lbl_46.config(text=gold)
    print('\nДеньги:', gold)
    list_inventory.remove(fire)
    lbl_14.config(text=list_inventory)
    lbl_29.config(text=list_inventory)
    lbl_52.config(text=list_inventory)
    print('Инвентарь:', list_inventory)
    min_bag -= 1
    lbl_12.config(text=(min_bag, '/', max_bag))
    lbl_27.config(text=(min_bag, '/', max_bag))
    lbl_48.config(text=(min_bag, '/', max_bag))
    print('Товаров в рюкзаке:', min_bag, '/', max_bag)
    if fire not in list_inventory:
        btn_15.config(state='disabled')
        lbl_38.config(fg='grey')
        lbl_52.config(text='Пусто')
        print('\nПродано:', fire)


# --------------------------------------- ГЛАВНОЕ ОКНО ---------------------------------------

root = Tk()
root.title('Собери рюкзак в поход')
root.geometry('400x600+900+150')
root.config(bg='grey')
root.resizable(False, False)

# --------------------------------------- ВКЛАДКИ ---------------------------------------

tab_control = ttk.Notebook(root)

tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_3 = ttk.Frame(tab_control)
tab_4 = ttk.Frame(tab_control)

tab_control.add(tab_1, text='Магазин')
tab_control.add(tab_2, text='Работа')
tab_control.add(tab_3, text='Инвентарь')
tab_control.add(tab_4, text='Продать')

tab_control.pack(expand=1, fill=BOTH)

# --------------------------------------- НАЧАЛЬНЫЕ РЕСУРСЫ ---------------------------------------

global gold, level, list_inventory, min_bag, max_bag
print('Деньги:', gold)
print('Уровень:', level)
print('Инвентарь:', list_inventory)

# --------------------------------------- ВКЛАДКА - МАГАЗИН ---------------------------------------

lbl_1 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_1.grid(row=0, column=0, columnspan=4)

lbl_2 = Label(tab_1, text='Добро пожаловать в магазин!', font=('Arial', 13, 'normal'))  # приветствие
lbl_2.grid(row=1, column=0, columnspan=4)

lbl_3 = Label(tab_1, text='Что вы хотите купить?', font=('Arial', 13, 'normal'))  # приветствие
lbl_3.grid(row=2, column=0, columnspan=4)

lbl_4 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_4.grid(row=3, column=0, columnspan=4)

# lbl_5 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))
# lbl_5.grid(row=6, column=0, columnspan=4)

lbl_6 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_6.grid(row=7, column=0, columnspan=4)

lbl_7 = Label(tab_1, text='Деньги:', font=('Arial', 13, 'normal'))  # надпись деньги
lbl_7.grid(row=16, column=0, sticky='w')

lbl_8 = Label(tab_1, text='Рюкзак:', font=('Arial', 13, 'normal'))  # надпись рюкзак
lbl_8.grid(row=17, column=0, sticky='w')

lbl_9 = Label(tab_1, text='Уровень:', font=('Arial', 13, 'normal'))  # надпись уровень
lbl_9.grid(row=18, column=0, sticky='w')

lbl_10 = Label(tab_1, text='Инвентарь:', font=('Arial', 13, 'normal'))  # надпись инвентарь
lbl_10.grid(row=19, column=0, sticky='w')

lbl_11 = Label(tab_1, text=gold, font=('Arial', 13, 'normal'))  # деньги
lbl_11.grid(row=16, column=1, sticky='w')

lbl_12 = Label(tab_1, text='0 / 3', font=('Arial', 13, 'normal'))  # заполненность рюкзака
lbl_12.grid(row=17, column=1, sticky='w')

lbl_13 = Label(tab_1, text=level, font=('Arial', 13, 'normal'))  # начальный уровень рюкзака
lbl_13.grid(row=18, column=1, sticky='w')

lbl_14 = Label(tab_1, text='Пусто', font=('Arial', 13, 'normal'))  # начальный инвентарь
lbl_14.grid(row=19, column=1, columnspan=15, sticky='w')

lbl_15 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'), fg='red')  # начальный пробел
lbl_15.grid(row=12, column=0, columnspan=4)

lbl_53 = Label(tab_1, text='100$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи палок
lbl_53.grid(row=5, column=0)

lbl_54 = Label(tab_1, text='60$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи газа
lbl_54.grid(row=5, column=1)

lbl_55 = Label(tab_1, text='20$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи зажигалки
lbl_55.grid(row=5, column=2)

lbl_56 = Label(tab_1, text='200$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи каремата
lbl_56.grid(row=5, column=3)

lbl_57 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_57.grid(row=6, column=0, columnspan=4)

lbl_58 = Label(tab_1, text='120$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи горелки
lbl_58.grid(row=8, column=0)

lbl_59 = Label(tab_1, text='80$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи посуды
lbl_59.grid(row=8, column=1)

lbl_60 = Label(tab_1, text='250$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи спальника
lbl_60.grid(row=8, column=2)

lbl_61 = Label(tab_1, text='50$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи фонаря
lbl_61.grid(row=8, column=3)

lbl_62 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_62.grid(row=9, column=0, columnspan=4)

lbl_63 = Label(tab_1, text='500$', font=('Arial', 13, 'normal'), fg='grey')  # цена понижения уровня рюкзака
lbl_63.grid(row=11, column=0, columnspan=4)

lbl_64 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_64.grid(row=12, column=0, columnspan=4)

lbl_65 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_65.grid(row=13, column=0, columnspan=4)

lbl_66 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_66.grid(row=14, column=0, columnspan=4)

lbl_67 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_67.grid(row=15, column=0, columnspan=4)


# кнопка - ПАЛКИ
btn_1 = Button(tab_1, text='Палки', font=('Arial', 13, 'normal'), width=9, command=stick_btn)
btn_1.grid(row=4, column=0, sticky='swen', padx=3, pady=3)

# кнопка - ГАЗ
btn_2 = Button(tab_1, text='Газ', font=('Arial', 13, 'normal'), width=9, command=gas_btn)
btn_2.grid(row=4, column=1, sticky='swen', padx=3, pady=3)

# кнопка - ЗАЖИГАЛКА
btn_3 = Button(tab_1, text='Зажигалка', font=('Arial', 13, 'normal'), width=9, command=lighter_btn)
btn_3.grid(row=4, column=2, sticky='swen', padx=3, pady=3)

# кнопка - КАРЕМАТ
btn_4 = Button(tab_1, text='Каремат', font=('Arial', 13, 'normal'), width=9, command=karemat_btn)
btn_4.grid(row=4, column=3, sticky='swen', padx=3, pady=3)

# кнопка - ГОРЕЛКА
btn_5 = Button(tab_1, text='Горелка', font=('Arial', 13, 'normal'), width=9, command=fire_btn)
btn_5.grid(row=7, column=0, sticky='swen', padx=3, pady=3)

# кнопка - ПОСУДА
btn_6 = Button(tab_1, text='Посуда', font=('Arial', 13, 'normal'), width=9, command=dishes_btn)
btn_6.grid(row=7, column=1, sticky='swen', padx=3, pady=3)

# кнопка - СПАЛЬНИК
btn_7 = Button(tab_1, text='Спальник', font=('Arial', 13, 'normal'), width=9, command=sleeping_bag_btn)
btn_7.grid(row=7, column=2, sticky='swen', padx=3, pady=3)

# кнопка - ФОНАРЬ
btn_8 = Button(tab_1, text='Фонарь', font=('Arial', 13, 'normal'), width=9, command=flashlight_btn)
btn_8.grid(row=7, column=3, sticky='swen', padx=3, pady=3)

# кнопка - ПОВЫСИТЬ УРОВЕНЬ РЮКЗАКА
btn_9 = Button(tab_1, text=level_bagpack, font=('Arial', 13, 'normal'), width=9, command=level_up)
btn_9.grid(row=10, column=0, columnspan=4, sticky='swen', padx=3, pady=3)

# --------------------------------------- ВКЛАДКА - РАБОТАТЬ ---------------------------------------

lbl_20 = Label(tab_2, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_20.grid(row=0, column=0, columnspan=4)

lbl_16 = Label(tab_2, text='Что, деньги закончились? ', font=('Arial', 13, 'normal'))  # приветствие
lbl_16.grid(row=1, column=0, columnspan=4)

lbl_17 = Label(tab_2, text='Кликай, чтобы заработать и покупай улучшения!', font=('Arial', 13, 'normal'))  # приветствие
lbl_17.grid(row=2, column=0, columnspan=4)

lbl_21 = Label(tab_2, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_21.grid(row=3, column=0, columnspan=4)

lbl_22 = Label(tab_2, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_22.grid(row=5, column=0, columnspan=4)

lbl_18 = Label(tab_2, text='Деньги:', font=('Arial', 13, 'normal'))  # начальная деньги
lbl_18.grid(row=6, column=0)

lbl_19 = Label(tab_2, text=gold, font=('Arial', 13, 'normal'))  # деньги
lbl_19.grid(row=6, column=1)



btn_10 = Button(tab_2, text='Работать', font=('Arial', 13, 'normal'), width=9, command=work)  # кнопка - Работать
btn_10.grid(row=4, column=0, columnspan=4, sticky='swen', padx=3, pady=3)

# --------------------------------------- ВКЛАДКА - ИНВЕНТАРЬ ---------------------------------------

lbl_23 = Label(tab_3, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_23.grid(row=0, column=0, columnspan=4)

lbl_24 = Label(tab_3, text=('Ваш рюкзак:'), font=('Arial', 13, 'normal'))  # приветствие
lbl_24.grid(row=1, column=0, columnspan=5)

lbl_25 = Label(tab_3, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_25.grid(row=2, column=0, columnspan=4)

lbl_26 = Label(tab_3, text='Деньги:', font=('Arial', 13, 'normal'))  # надпись деньги
lbl_26.grid(row=3, column=0, sticky='w')

lbl_26 = Label(tab_3, text=gold, font=('Arial', 13, 'normal'))  # начальная деньги
lbl_26.grid(row=3, column=1, sticky='w')

lbl_27 = Label(tab_3, text='Рюкзак:', font=('Arial', 13, 'normal'))  # надпись рюкзак
lbl_27.grid(row=4, column=0, sticky='w')

lbl_27 = Label(tab_3, text='0 / 3', font=('Arial', 13, 'normal'))  # начальная уровень рюкзака
lbl_27.grid(row=4, column=1, sticky='w')

lbl_28 = Label(tab_3, text='Уровень:', font=('Arial', 13, 'normal'))  # надпись уровень
lbl_28.grid(row=5, column=0, sticky='w')

lbl_28 = Label(tab_3, text=level, font=('Arial', 13, 'normal'))  # начальная уровень
lbl_28.grid(row=5, column=1, sticky='w')

lbl_29 = Label(tab_3, text='Инвентарь:', font=('Arial', 13, 'normal'))  # надпись инвентарь
lbl_29.grid(row=6, column=0, sticky='w')

lbl_29 = Label(tab_3, text='Пусто', font=('Arial', 13, 'normal'))  # начальная инвентарь
lbl_29.grid(row=6, column=1, sticky='w')

# --------------------------------------- ВКЛАДКА - ПРОДАТЬ ---------------------------------------

lbl_30 = Label(tab_4, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_30.grid(row=0, column=0, columnspan=4)

lbl_31 = Label(tab_4, text='Здесь вы можете продать товары', font=('Arial', 13, 'normal'))  # приветствие
lbl_31.grid(row=1, column=0, columnspan=4)

lbl_32 = Label(tab_4, text='Что хотите продать?', font=('Arial', 13, 'normal'))  # приветствие
lbl_32.grid(row=2, column=0, columnspan=4)

lbl_33 = Label(tab_4, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_33.grid(row=3, column=0, columnspan=4)

lbl_34 = Label(tab_4, text='70$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи палок
lbl_34.grid(row=5, column=0)

lbl_35 = Label(tab_4, text='42$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи газа
lbl_35.grid(row=5, column=1)

lbl_36 = Label(tab_4, text='14$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи зажигалки
lbl_36.grid(row=5, column=2)

lbl_37 = Label(tab_4, text='140 $', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи каремата
lbl_37.grid(row=5, column=3)

lbl_43 = Label(tab_4, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_43.grid(row=6, column=0, columnspan=4)

lbl_38 = Label(tab_4, text='84$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи горелки
lbl_38.grid(row=8, column=0)

lbl_39 = Label(tab_4, text='56$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи посуды
lbl_39.grid(row=8, column=1)

lbl_40 = Label(tab_4, text='175$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи спальника
lbl_40.grid(row=8, column=2)

lbl_41 = Label(tab_4, text='35$', font=('Arial', 13, 'normal'), fg='grey')  # цена продажи фонаря
lbl_41.grid(row=8, column=3)

lbl_42 = Label(tab_4, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_42.grid(row=9, column=0, columnspan=4)

lbl_42 = Label(tab_4, text='350$', font=('Arial', 13, 'normal'), fg='grey')  # цена понижения уровня рюкзака
lbl_42.grid(row=11, column=0, columnspan=4)

lbl_44 = Label(tab_4, text=' ', font=('Arial', 13, 'normal'))  # пробел
lbl_44.grid(row=12, column=0, columnspan=4)

lbl_45 = Label(tab_4, text='Деньги:', font=('Arial', 13, 'normal'))  # надпись деньги
lbl_45.grid(row=13, column=0, sticky='w')

lbl_46 = Label(tab_4, text=gold, font=('Arial', 13, 'normal'))  # начальная деньги
lbl_46.grid(row=13, column=1, sticky='w')

lbl_47 = Label(tab_4, text='Рюкзак:', font=('Arial', 13, 'normal'))  # надпись рюкзак
lbl_47.grid(row=14, column=0, sticky='w')

lbl_48 = Label(tab_4, text='0 / 3', font=('Arial', 13, 'normal'))  # начальная уровень рюкзака
lbl_48.grid(row=14, column=1, sticky='w')

lbl_49 = Label(tab_4, text='Уровень:', font=('Arial', 13, 'normal'))  # надпись уровень
lbl_49.grid(row=15, column=0, sticky='w')

lbl_50 = Label(tab_4, text=level, font=('Arial', 13, 'normal'))  # начальная уровень
lbl_50.grid(row=15, column=1, sticky='w')

lbl_51 = Label(tab_4, text='Инвентарь:', font=('Arial', 13, 'normal'))  # надпись инвентарь
lbl_51.grid(row=16, column=0, sticky='w')

lbl_52 = Label(tab_4, text='Пусто', font=('Arial', 13, 'normal'))  # начальная инвентарь
lbl_52.grid(row=16, column=1, columnspan=15, sticky='w')



# кнопка - ПРОДАТЬ ПАЛКИ
btn_11 = Button(tab_4, text='Палки', font=('Arial', 13, 'normal'), width=9, state='disabled', command=sell_stick_btn)
btn_11.grid(row=4, column=0, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ ГАЗ
btn_12 = Button(tab_4, text='Газ', font=('Arial', 13, 'normal'), width=9, state='disabled', command=sell_gas_btn)
btn_12.grid(row=4, column=1, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ ЗАЖИГАЛКА
btn_13 = Button(tab_4, text='Зажигалка', font=('Arial', 13, 'normal'), width=9, state='disabled',
                command=sell_lighter_btn)
btn_13.grid(row=4, column=2, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ КАРЕМАТ
btn_14 = Button(tab_4, text='Каремат', font=('Arial', 13, 'normal'), width=9, state='disabled', command=sell_karemat_btn)
btn_14.grid(row=4, column=3, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ ГОРЕЛКА
btn_15 = Button(tab_4, text='Горелка', font=('Arial', 13, 'normal'), width=9, state='disabled', command=sell_fire_btn)
btn_15.grid(row=7, column=0, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ ПОСУДА
btn_16 = Button(tab_4, text='Посуда', font=('Arial', 13, 'normal'), width=9, state='disabled', command=dishes_btn)
btn_16.grid(row=7, column=1, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ СПАЛЬНИК
btn_17 = Button(tab_4, text='Спальник', font=('Arial', 13, 'normal'), width=9, state='disabled',
                command=sleeping_bag_btn)
btn_17.grid(row=7, column=2, sticky='swen', padx=3, pady=3)

# кнопка - ПРОДАТЬ ФОНАРЬ
btn_18 = Button(tab_4, text='Фонарь', font=('Arial', 13, 'normal'), width=9, state='disabled', command=flashlight_btn)
btn_18.grid(row=7, column=3, sticky='swen', padx=3, pady=3)

# кнопка - ПОНИЗИТЬ УРОВЕНЬ РЮКЗАКА
btn_19 = Button(tab_4, text=level_bagpack_low, font=('Arial', 13, 'normal'), width=9, state='disabled',
                command=level_up)
btn_19.grid(row=10, column=0, columnspan=4, sticky='swen', padx=3, pady=3)

# --------------------------------------- СИСТЕМНОЕ ---------------------------------------

root.mainloop()
