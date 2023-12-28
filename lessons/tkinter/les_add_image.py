from tkinter import *

root = Tk ()
root.title ('Фон - Картинка')
root.geometry ('500x500+200+200')
root.config (bg = '')
root.resizable(False, False)

root.image = PhotoImage(file='fon.png')
bg_image = Label(root, image=root.image)
bg_image.place(relx=0.5, rely=0.5, anchor=CENTER)

btn = Button(root, text='TEST')
btn.place(x=50, y=50)

root.mainloop ()