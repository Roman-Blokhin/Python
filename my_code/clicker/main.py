from tkinter import *

count = 0


def click():
    global count
    count += 1
    counter.config(text=count)

root = Tk()
root.title('Кликер')
root.geometry('250x250+200+200')
root.config(bg='black')

counter = Label(root, text='0', font=('Arial 55'), bg='black', fg='white')
counter.pack()

clicker = Button(root, text='Нажми', font=('Arial 20'), command=click)
clicker.pack()

root.mainloop()
