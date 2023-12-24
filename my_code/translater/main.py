from tkinter import *
from googletrans import Translator

root = Tk ()
root.title ('Переводчик')
root.geometry ('500x500+200+200')
root['bg'] = 'black'
root.resizable(width=False, height=False)

tranlator = Translator

lbl_1 = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст:')
lbl_1.pack()


root.mainloop ()