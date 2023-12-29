from tkinter import *
from tkinter import ttk

root = Tk ()
root.title ('Вкладки')
root.geometry ('350x350+200+200')
root.config (bg = '')
root.resizable(False, False)

tab_control = ttk.Notebook(root)  # создаем панель вкладок

tab1 = ttk.Frame(tab_control)  # создаем фреймы для вкладок
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Первая')  # размещаем наши фреймы на панели вкладок
tab_control.add(tab2, text='Вторая')

lbl_1 = Label(tab1, text='Вот это че за новая страница')
lbl_1.pack()

lbl_2 = Label(tab2, text='Крутяк, новая вкладка')
lbl_2.pack()

tab_control.pack(expand=1, fill=BOTH)

root.mainloop ()