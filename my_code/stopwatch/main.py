from tkinter import *
from datetime import *

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


root = Tk()
root.title('')
root.geometry('450x480+200+200')
root.config(bg='black')

label_1 = Label(root, text='00:00', bg='black', fg='white', font=('Arial 30'))
label_1.pack()

btn_start = Button(root, text='Старт', bg='black', fg='white', font=('Arial 20'), width=15, command=start_tick)
btn_start.pack()

btn_stop = Button(root, text='Стоп', bg='black', fg='white', font=('Arial 20'), width=15)
btn_continue = Button(root, text='Продолжить', bg='black', fg='white', font=('Arial 20'), width=15)
btn_reset = Button(root, text='Сбросить', bg='black', fg='white', font=('Arial 20'), width=15)

root.mainloop()
