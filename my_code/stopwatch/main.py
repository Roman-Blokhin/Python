from tkinter import *
from datetime import *


def know_time():
    now = datetime.now()
    timing = now.strftime('%H:%M:%S')
    times.config(text=timing)


root = Tk()
root.title('')
root.geometry('450x180+200+200')
root.config(bg='black')

times = Label(root, text='0', bg='black', fg='white', font=('Arial 50'))
times.pack()

time_button = Button(root, text='Узнать время', bg='black', fg='white', font=('Arial 20'), command=know_time)
time_button.pack()

root.mainloop()
