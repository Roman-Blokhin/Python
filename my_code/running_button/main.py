from tkinter import *
from tkinter import messagebox
import random as r


def no():
    messagebox.showinfo('Информация', 'Спасибо, ваш голос учтен')
    root.destroy()


def yes(event):
    yes_btn.place(x=r.randint(10, 280), y=r.randint(10, 280))


root = Tk()
root.title('Бегающая кнопка')
root.geometry('300x300+200+200')
root.config(bg='')
root.resizable(False, False)

info = Label(root, text='Хочешь ли ты повышения зарплаты?', font='Arial 10 bold')
info.pack()

yes_btn = Button(root, text='Да', font='Arial 15 bold')
yes_btn.place(x=70, y=100)

yes_btn.bind('<Enter>', yes)

no_btn = Button(root, text='Нет', font='Arial 15 bold', command=no)
no_btn.place(x=200, y=100)



root.mainloop()
