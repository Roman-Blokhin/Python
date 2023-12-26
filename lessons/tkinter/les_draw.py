from tkinter import *

root = Tk()
root.title('Рисование')
root.geometry('700x500+200+200')
root.config(bg='grey')
root.resizable(False, False)

canvas = Canvas(root, bg='white', width=650, height=450)  # разместили холст в окне
canvas.place(x=25, y=25)

canvas.create_rectangle(20, 20, 100, 100, width=5, fill='lime', outline='brown')  # нарисовали прямоугольник

root.mainloop()
