from tkinter import *
from datetime import *


def know_time():
    now = datetime.now()
    timing = now.strftime('%H:%M:%S')
    times.config(text=timing)


root = Tk()
root.title('')
root.geometry('450x480+200+200')
root.config(bg='black')

label_1 = Label(root, text='00:00', bg='black', fg='white', font=('Arial 30'))
label_1.pack()

btn_start = Button(root, text='Старт', bg='black', fg='white', font=('Arial 20'), width=15)
btn_start.pack()

btn_stop = Button(root, text='Стоп', bg='black', fg='white', font=('Arial 20'), width=15)
btn_stop.pack()

btn_continie = Button(root, text='Продолжить', bg='black', fg='white', font=('Arial 20'), width=15)
btn_continie.pack()

btn_reset = Button(root, text='Сбросить', bg='black', fg='white', font=('Arial 20'), width=15)
btn_reset.pack()
# ----------------------------------- Время сейчас ----------------------------

times = Label(root, text='0', bg='black', fg='white', font=('Arial 50'))
times.pack()

time_button = Button(root, text='Узнать время', bg='black', fg='white', font=('Arial 20'), command=know_time)
time_button.pack()

root.mainloop()
