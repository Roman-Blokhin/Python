from tkinter import *
from tkinter import messagebox


def no():
    messagebox.showinfo('Информация', 'Спасибо, ваш голос учтен')
    root.destroy()

root = Tk ()
root.title ('Бегающая кнопка')
root.geometry ('300x300+200+200')
root.config (bg = '')
root.resizable(False, False)

info = Label(root, text='Хочешь ли ты повышения зарплаты?', font='Arial 10 bold')
info.pack()

yes_btn = Button(root, text='Да', font='Arial 15 bold')
yes_btn.place(x=70, y=100)

yes_btn = Button(root, text='Нет', font='Arial 15 bold', command=no)
yes_btn.place(x=200, y=100)

root.mainloop ()