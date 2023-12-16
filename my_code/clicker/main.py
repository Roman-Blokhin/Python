from tkinter import *
from math import floor

count = 0
count_100 = 0


def click():
    global count
    global count_100
    count += 1
    counter.config(text=count)
    count_100 = count / 100
    counter_100.config(text=floor(count_100))


root = Tk()
root.title('Кликер')
root.geometry('250x250+200+200')
root.config(bg='black')

counter = Label(root, text='0', font=('Arial 55'), bg='black', fg='white')
counter.pack()

clicker = Button(root, text='Нажми', font=('Arial 20'), command=click)
clicker.pack()

counter_100 = Label(root, text='0', font=('Arial 55'), bg='black', fg='white')
counter_100.pack()

root.mainloop()
