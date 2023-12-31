from tkinter import *


def popup():
    pass


root = Tk()
root.title('Контекстное меню')
root.geometry('350x350+200+200')
root.config(bg='')
root.resizable(False, False)

c = Canvas(root, width=300, height=300, bg='white')  # создали холст для контекстного меню
c.pack()

c.bind('<Button-3>', popup)  # забиндили ПКМ, подключили функцию

root.mainloop()
