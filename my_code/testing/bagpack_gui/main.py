from tkinter import *
from tkinter import ttk


# --------------------------------------- ФУНКЦИИ ---------------------------------------

def first():
    pass

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

lbl_1 = Label(tab_1, text='Добро пожаловать в магазин!', font=('Arial', 13, 'normal'))
lbl_1.grid(row=0, column=0, columnspan=8)

lbl_1 = Label(tab_1, text='Что вы хотите купить?', font=('Arial', 13, 'normal'))
lbl_1.grid(row=1, column=0, columnspan=8)

btn_1 = Button(tab_1, text='Палки', font=('Arial', 13, 'normal'))
btn_1.grid(row=2, column=0, sticky='swen', padx=3, pady=3)

# --------------------------------------- СИСТЕМНОЕ ---------------------------------------

root.mainloop()
