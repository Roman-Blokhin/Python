from tkinter import *
from tkinter import ttk
from vars import *


# --------------------------------------- ПЕРЕМЕННЫЕ ---------------------------------------



# --------------------------------------- ФУНКЦИИ ---------------------------------------

def stick_btn():
    global gold, list_inventory
    if gold < sticks_cost:
        gold += 0
        lbl_11.config(text=gold)
        lbl_15 = Label(tab_1, text=no_money, font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        print(no_money)
    else:
        gold -= sticks_cost
        lbl_11.config(text=gold)
        print(gold)
        list_inventory.append('Палки')
        lbl_14.config(text=list_inventory)
        print(list_inventory)


def level_up():
    global gold, level
    if gold >= level_bagpack_cost:
        gold -= level_bagpack_cost
        level += 1
        lbl_11.config(text=gold)
        lbl_13.config(text=level)
        print(gold)
        print(level)
    else:
        lbl_15 = Label(tab_1, text='Нет денег, идите работать!', font=('Arial', 13, 'normal'), fg='red')
        lbl_15.grid(row=12, column=0, columnspan=4)
        gold -= 0
        level += 0


# --------------------------------------- ГЛАВНОЕ ОКНО ---------------------------------------

root = Tk()
root.title('Собери рюкзак в поход')
root.geometry('400x400+200+200')
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


lbl_1 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))
lbl_1.grid(row=0, column=0, columnspan=4)

lbl_2 = Label(tab_1, text='Добро пожаловать в магазин!', font=('Arial', 13, 'normal'))
lbl_2.grid(row=1, column=0, columnspan=4)

lbl_3 = Label(tab_1, text='Что вы хотите купить?', font=('Arial', 13, 'normal'))
lbl_3.grid(row=2, column=0, columnspan=4)

lbl_4 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))
lbl_4.grid(row=3, column=0, columnspan=4)

# lbl_5 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))
# lbl_5.grid(row=6, column=0, columnspan=4)

lbl_6 = Label(tab_1, text=' ', font=('Arial', 13, 'normal'))
lbl_6.grid(row=7, column=0, columnspan=4)

lbl_7 = Label(tab_1, text='Деньги:', font=('Arial', 13, 'normal'))
lbl_7.grid(row=8, column=0, sticky='w')

lbl_8 = Label(tab_1, text='Рюкзак:', font=('Arial', 13, 'normal'))
lbl_8.grid(row=9, column=0, sticky='w')

lbl_9 = Label(tab_1, text='Уровень:', font=('Arial', 13, 'normal'))
lbl_9.grid(row=10, column=0, sticky='w')

lbl_10 = Label(tab_1, text='Инвентарь:', font=('Arial', 13, 'normal'))
lbl_10.grid(row=11, column=0, sticky='w')

lbl_11 = Label(tab_1, text='300', font=('Arial', 13, 'normal'))
lbl_11.grid(row=8, column=1, sticky='w')

lbl_12 = Label(tab_1, text='0/3', font=('Arial', 13, 'normal'))
lbl_12.grid(row=9, column=1, sticky='w')

lbl_13 = Label(tab_1, text='1', font=('Arial', 13, 'normal'))
lbl_13.grid(row=10, column=1, sticky='w')

lbl_14 = Label(tab_1, text='Пусто', font=('Arial', 13, 'normal'))
lbl_14.grid(row=11, column=1, columnspan=10, sticky='w')



btn_1 = Button(tab_1, text='Палки', font=('Arial', 13, 'normal'), width=9, command=stick_btn)
btn_1.grid(row=4, column=0, sticky='swen', padx=3, pady=3)

btn_2 = Button(tab_1, text='Газ', font=('Arial', 13, 'normal'), width=9)
btn_2.grid(row=4, column=1, sticky='swen', padx=3, pady=3)

btn_3 = Button(tab_1, text='Зажигалка', font=('Arial', 13, 'normal'), width=9)
btn_3.grid(row=4, column=2, sticky='swen', padx=3, pady=3)

btn_4 = Button(tab_1, text='Каремат', font=('Arial', 13, 'normal'), width=9)
btn_4.grid(row=4, column=3, sticky='swen', padx=3, pady=3)

btn_5 = Button(tab_1, text='Горелка', font=('Arial', 13, 'normal'), width=9)
btn_5.grid(row=5, column=0, sticky='swen', padx=3, pady=3)

btn_6 = Button(tab_1, text='Посуда', font=('Arial', 13, 'normal'), width=9)
btn_6.grid(row=5, column=1, sticky='swen', padx=3, pady=3)

btn_7 = Button(tab_1, text='Спальник', font=('Arial', 13, 'normal'), width=9)
btn_7.grid(row=5, column=2, sticky='swen', padx=3, pady=3)

btn_8 = Button(tab_1, text='Фонарь', font=('Arial', 13, 'normal'), width=9)
btn_8.grid(row=5, column=3, sticky='swen', padx=3, pady=3)

btn_9 = Button(tab_1, text=level_bagpack, font=('Arial', 13, 'normal'), width=9, command=level_up)
btn_9.grid(row=6, column=0, columnspan=4, sticky='swen', padx=3, pady=3)

# --------------------------------------- СИСТЕМНОЕ ---------------------------------------


root.mainloop()
