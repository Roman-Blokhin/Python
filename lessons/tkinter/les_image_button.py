from tkinter import *
from PIL import ImageTk

root = Tk ()
root.title ('Кнопки с картинками')
root.geometry ('350x350+200+200')
root.config (bg = '')
root.resizable(False, False)

im_python = ImageTk.PhotoImage(file='python.png')  # подтягиваем картинку в программу

btn_python = Button(root, height=100, text='Python', image=im_python, compound=TOP)  # compound=TOP - располож. карт.
btn_python.pack()

root.mainloop ()