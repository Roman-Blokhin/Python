from tkinter import *
import random as r

click = 0


def running_btn():
    global click
    btn_click.place(x=r.randint(10, 400), y=r.randint(10, 400))
    click += 1
    clicker.config(text=click)


root = Tk()
root.title('Бегающая кнопка')
root.geometry('600x600+100+100')
root.config(bg='pink')

btn_click = Button(root, text='Кликай', bg='grey', fg='white', font='Arial 20', command=running_btn)
btn_click.place(x=r.randint(10, 450), y=r.randint(10, 450))

clicker = Label(root, text='0', bg='pink', fg='black', font='Arial 30')
clicker.pack(expand=1)

root.mainloop()
