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
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= sticks_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(sticks)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)


def gas_btn():  # кнопка - ГАЗ
    global gold, list_inventory, min_bag, max_bag
    if gold < gas_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= gas_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(gas)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)


def lighter_btn():  # кнопка - ЗАЖИГАЛКА
    global gold, list_inventory, min_bag, max_bag
    if gold < lighter_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= lighter_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(lighter)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)


def karemat_btn():  # кнопка - КАРЕМАТ
    global gold, list_inventory, min_bag, max_bag
    if gold < karemat_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= karemat_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(karemat)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)


def fire_btn():  # кнопка - ГОРЕЛКА
    global gold, list_inventory, min_bag, max_bag
    if gold < fire_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= fire_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(fire)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)


def dishes_btn():  # кнопка - ПОСУДА
    global gold, list_inventory, min_bag, max_bag
    if gold < dishes_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= dishes_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(dishes)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)



def sleeping_bag_btn():  # кнопка - СПАЛЬНИК
    global gold, list_inventory, min_bag, max_bag
    if gold < sleeping_bag_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        if min_bag < max_bag:
            gold -= sleeping_bag_cost
            lbl_11.config(text=gold)
            print('Деньги:', gold)
            list_inventory.append(sleeping_bag)
            lbl_14.config(text=list_inventory)
            print('Инвентарь:', list_inventory)
            min_bag += 1
            lbl_12.config(text=(min_bag, '/', max_bag))
            print('Товаров в рюкзаке:', min_bag, '/', max_bag)
        else:
            min_bag += 0
            gold += 0
            lbl_16 = Label(tab_1, text=full_bag, font=('Arial', 13, 'normal'), fg='red')
            lbl_16.grid(row=13, column=0, columnspan=4)
            print(full_bag)


def level_up():
    global gold, level
    if gold >= level_bagpack_cost:
        gold -= level_bagpack_cost
        level += 1
        lbl_11.config(text=gold)
        lbl_13.config(text=level)
        print(gold)
        print(level)
        lbl_12.config(text=(min_bag, '/', max_bag + 5))
    else:
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        gold -= 0
        level += 0


# --------------------------------------- ГЛАВНОЕ ОКНО ---------------------------------------

root = Tk()
root.title('Собери рюкзак в поход')
root.geometry('390x500+200+200')
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

# --------------------------------------- ПАНЕЛЬ РЕСУРСОВ ---------------------------------------



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
lbl_7.grid(row=8, column=0, sticky='w')

lbl_8 = Label(tab_1, text='Рюкзак:', font=('Arial', 13, 'normal'))  # надпись рюкзак
lbl_8.grid(row=9, column=0, sticky='w')

lbl_9 = Label(tab_1, text='Уровень:', font=('Arial', 13, 'normal'))  # надпись уровень
lbl_9.grid(row=10, column=0, sticky='w')

lbl_10 = Label(tab_1, text='Инвентарь:', font=('Arial', 13, 'normal'))  # надпись инвентарь
lbl_10.grid(row=11, column=0, sticky='w')

lbl_11 = Label(tab_1, text='500', font=('Arial', 13, 'normal'))  # деньги
lbl_11.grid(row=8, column=1, sticky='w')

lbl_12 = Label(tab_1, text='0 / 3', font=('Arial', 13, 'normal'))  # заполненность рюкзака
lbl_12.grid(row=9, column=1, sticky='w')

lbl_13 = Label(tab_1, text='1', font=('Arial', 13, 'normal'))  # начальный уровень рюкзака
lbl_13.grid(row=10, column=1, sticky='w')

lbl_14 = Label(tab_1, text='Пусто', font=('Arial', 13, 'normal'))  # начальный инвентарь
lbl_14.grid(row=11, column=1, columnspan=10, sticky='w')

lbl_15 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'), fg='red')  # начальный пробел
lbl_15.grid(row=12, column=0, columnspan=4)


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
btn_5.grid(row=5, column=0, sticky='swen', padx=3, pady=3)

# кнопка - ПОСУДА
btn_6 = Button(tab_1, text='Посуда', font=('Arial', 13, 'normal'), width=9, command=dishes_btn)
btn_6.grid(row=5, column=1, sticky='swen', padx=3, pady=3)

# кнопка - СПАЛЬНИК
btn_7 = Button(tab_1, text='Спальник', font=('Arial', 13, 'normal'), width=9, command=sleeping_bag_btn)
btn_7.grid(row=5, column=2, sticky='swen', padx=3, pady=3)

# кнопка - ФОНАРЬ
btn_8 = Button(tab_1, text='Фонарь', font=('Arial', 13, 'normal'), width=9)
btn_8.grid(row=5, column=3, sticky='swen', padx=3, pady=3)

# кнопка - ПОВЫСИТЬ УРОВЕНЬ РЮКЗАКА
btn_9 = Button(tab_1, text=level_bagpack, font=('Arial', 13, 'normal'), width=9, command=level_up)
btn_9.grid(row=6, column=0, columnspan=4, sticky='swen', padx=3, pady=3)

# --------------------------------------- СИСТЕМНОЕ ---------------------------------------


root.mainloop()
