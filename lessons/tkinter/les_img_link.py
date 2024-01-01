from tkinter import *
import requests  # позволяет работать с HTTP-запросами
from io import BytesIO
from PIL import ImageTk, Image


def load_img():
    pass


root = Tk()
root.title('')
root.geometry('400x400+200+200')
root.config(bg='')
root.resizable(False, False)

btn = Button(root, text='Установить фон', command=load_img)
btn.pack()

lbl = Label(root)
lbl.pack()

root.mainloop()
