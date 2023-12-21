from tkinter import *


def open_toplevel():
    pass


root = Tk()
root.title('')
root.geometry('350x350+200+200')
root.config(bg='')
root.resizable(width=False, height=False)

btn = Button(root, text='Открыть', command=open_toplevel)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
