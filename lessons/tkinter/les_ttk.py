# СТИЛИ В TKINTER - TTK
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('')
root.geometry('350x350+200+200')
root.config(bg='')
root.resizable(width=False, height=False)

# можно изменять стили объектов
s = ttk.Style()  # присвоили объект классу Style
print(s.theme_names())  # выводит в консоль стили, которые есть
print(s.theme_use())  # показывает, какой стиль у меня
print(s.theme_use('classic'))  # позволяет выбрать стиль самостоятельно
#s.configure('.', foreground='red')  # '.' - говорит, что изменение стиля повлияет на все объекты ttk
s.configure('TButton', foreground='blue')  # 'T...' - T обязательно ставим, если нужно применить стиль к опр. виджету

# стандартная кнопка
Button(root, text='Один', padx=10).pack()

# кнопка под стиль ОС
ttk.Button(root, text='Два', width=20).pack()

Entry(root).pack()
ttk.Entry(root).pack()

root.mainloop()
