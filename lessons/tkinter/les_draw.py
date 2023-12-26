from tkinter import *

root = Tk()
root.title('Рисование')
root.geometry('700x500+200+200')
root.config(bg='grey')
root.resizable(False, False)

canvas = Canvas(root, bg='white', width=650, height=450)  # разместили холст в окне
canvas.place(x=25, y=25)

canvas.create_rectangle(20, 20, 100, 100, width=5, fill='lime', outline='brown')  # прямоугольник

canvas.create_line(120, 20, 200, 100, width=5, fill='red')  # линия

canvas.create_arc(150, 250, 350, 380)  # угол

canvas.create_oval(300, 350, 400, 450, fill='yellow', width=3)  # круг

canvas.create_oval(500, 50, 300, 150, fill='red', width=10)  # овал

canvas.create_polygon(500, 250, 550, 360, 600, 400, 650, 30)  # многоугольник

root.mainloop()
