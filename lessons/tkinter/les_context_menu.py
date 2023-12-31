from tkinter import *
from random import randint


# ------------------------- Функции ------------------------

def popup(event):  # функция для создания всплывающего контекстного меню в месте нажатия ПКМ
    global x, y
    x = event.x
    y = event.y
    popup_menu.post(event.x_root, event.y_root)


def circle():
    c.create_oval(randint(10, 380), randint(10, 380), randint(10, 380), randint(10, 380), fill='red')


def square():
    c.create_rectangle(randint(10, 380), randint(10, 380), randint(10, 380), randint(10, 380), fill='lime')


# ------------------------- Переменные ------------------------

x = 0
y = 0

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
popup_menu.add_command(label='Открыть', command=circle)
popup_menu.add_command(label='Создать', command=square)
popup_menu.add_command(label='Отправить', command=circle)
popup_menu.add_command(label='Удалить', command=square)

# ------------------------- Важное ------------------------

root.mainloop()
