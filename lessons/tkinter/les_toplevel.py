from tkinter import *


def open_toplevel():
    win = Toplevel()  # виджет, который создает новое окно поверх первого, с его же настройками
    win.geometry('200x200+700+400')
    # win.grab_set()  # не позволяет закрывать программу, если открыто новое окно
    l1 = Label(win, text='Toplevel', font='Arial 15 bold', fg='brown')
    l1.pack()
    win.overrideredirect(1)  # убирает верхнюю панель с функциями у дочернего окна, значение (0), возвращает панель


root = Tk()
root.title('Test')
root.geometry('350x350+200+200')
root.config(bg='')
root.resizable(width=False, height=False)

btn = Button(root, text='Открыть', command=open_toplevel)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
