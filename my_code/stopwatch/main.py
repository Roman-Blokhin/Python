import datetime
from tkinter import *
from datetime import *
import time

temp = 0
after_id = ''


# функция, которая берет начало отсчета от 0 и меняет наши параметры на 1 с частотой в 1 секунду
def tick():
    global temp, after_id
    after_id = root.after(1000, tick)  # after - запускает действие через количество миллисекунд. 1000 = 1 секунда
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')  # fromtimestamp - начало точки отсчета, temp = 0
    label_1.config(text=str(f_temp))
    temp += 1


def start_tick():
    btn_start.pack_forget()  # убираем размещение нашей кнопки - Старт, на экране
    btn_stop.pack()  # размещаем кнопку - Стоп
    tick()  # вызываем функцию для запуска секундомера


def stop_tick():
    root.after_cancel(after_id)
    btn_stop.pack_forget()
    btn_continue.pack()  # вывели новые кнопки
    btn_reset.pack()


def continue_tick():
    btn_continue.pack_forget()
    btn_reset.pack_forget()
    btn_stop.pack()
    tick()


def reset_tick():
    global temp
    temp = 0  # обнуляем наш секундомер
    label_1.config(text='00:00')  # выводим надпись на место секундомера
    btn_reset.pack_forget()
    btn_continue.pack_forget()
    btn_start.pack()


def show_time():  # функция, которая показывает время сейчас
    now = time.strftime('%H:%M:%S')
    root.after(1000, show_time)
    label_2.config(text=now)


root = Tk()
root.title('')
root.geometry('450x480+200+200')
root.config(bg='black')

label_1 = Label(root, text='00:00', bg='black', fg='white', font=('Arial 30'))
label_1.pack()

btn_start = Button(root, text='Старт', bg='black', fg='white', font=('Arial 20'), width=15, command=start_tick)
btn_start.pack()

btn_stop = Button(root, text='Стоп', bg='black', fg='white', font=('Arial 20'), width=15, command=stop_tick)
btn_continue = Button(root, text='Продолжить', bg='black', fg='white', font=('Arial 20'), width=15,
                      command=continue_tick)
btn_reset = Button(root, text='Сбросить', bg='black', fg='white', font=('Arial 20'), width=15, command=reset_tick)

# ------------------------------ Время сейчас ------------------------------

label_2 = Label(root, text='00:00:00', bg='black', fg='white', font=('Arial 30'))
label_2.place(x=250, y=300)

label_3 = Label(root, text='Время:', bg='black', fg='white', font=('Arial 30'))
label_3.place(x=50, y=300)

show_time()

root.mainloop()
