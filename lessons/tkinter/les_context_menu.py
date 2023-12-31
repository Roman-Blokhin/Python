from tkinter import *


# ------------------------- Функции ------------------------

def popup():
    pass


def circle():
    pass


def square():
    pass


# ------------------------- Окно ------------------------

root = Tk()
root.title('Контекстное меню')
root.geometry('350x350+200+200')
root.config(bg='')
root.resizable(False, False)

# ------------------------- Холст и клавиша мыши ------------------------

c = Canvas(root, width=300, height=300, bg='white')  # создали холст для контекстного меню
c.pack()

c.bind('<Button-3>', popup)  # забиндили ПКМ, подключили функцию

# ------------------------- Меню ------------------------

popup_menu = Menu(tearoff=0)

popup_menu.add_command(label='Круг', command=circle)
popup_menu.add_command(label='Квадрат', command=square)

# ------------------------- Важное ------------------------

root.mainloop()
