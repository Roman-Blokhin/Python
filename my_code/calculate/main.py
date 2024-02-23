from tkinter import *
from tkinter import messagebox


# ------------------------------- ФУНКЦИИ -------------------------------

def calculate_exit():
    answer = messagebox.askokcancel('Выход', 'Действительно выйти?')
    if answer:
        root.destroy()


# прописывает значение в окно вывода
def first(digit):
    value = entry.get() + str(digit)  # добавляет цифру в окошко
    if value[0] == '0':
        value = value[1:]  # заменяет первоначальный 0 на цифру
    entry.delete(0, END)  # очищает окно
    entry.insert(0, value)  # вставляет цифру
    print('1')


# создаем шаблон кнопки, в которой одинаковые значения для всех цифр, цифру указываем - digit
def make_button(digit):
    return Button(root, text=digit, font=('Comic Sans MS', 15, 'normal'), command=lambda: first(digit))


# ------------------------------- ОКНО -------------------------------

root = Tk()
root.title('Калькулятор')
root.geometry('400x400+200+200')
root.config(bg='Grey')
root.resizable(False, False)
# root.protocol('WM_DELETE_WINDOW', calculate_exit)

# ------------------------------- ОКНО ВЫВОДА -------------------------------

entry = Entry(root, width=15, font=('Comic Sans MS', 20, 'normal'), justify=RIGHT)
entry.insert(0, '0')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# ------------------------------- КНОПКИ -------------------------------

make_button(1).grid(row=1, column=0, sticky='swen', padx=3, pady=3)
make_button(2).grid(row=1, column=1, sticky='swen', padx=3, pady=3)
make_button(3).grid(row=1, column=2, sticky='swen', padx=3, pady=3)
make_button(4).grid(row=2, column=0, sticky='swen', padx=3, pady=3)
make_button(5).grid(row=2, column=1, sticky='swen', padx=3, pady=3)
make_button(6).grid(row=2, column=2, sticky='swen', padx=3, pady=3)
make_button(7).grid(row=3, column=0, sticky='swen', padx=3, pady=3)
make_button(8).grid(row=3, column=1, sticky='swen', padx=3, pady=3)
make_button(9).grid(row=3, column=2, sticky='swen', padx=3, pady=3)
make_button(0).grid(row=4, column=0, sticky='swen', padx=3, pady=3)

# ------------------------------- КНОПКИ ДЕЙСТВИЙ -------------------------------

btn11 = Button(root, text='/', font=('Comic Sans MS', 15, 'normal'))
btn11.grid(row=1, column=3, sticky='swen', padx=3, pady=3)

btn12 = Button(root, text='*', font=('Comic Sans MS', 15, 'normal'))
btn12.grid(row=2, column=3, sticky='swen', padx=3, pady=3)

btn13 = Button(root, text='-', font=('Comic Sans MS', 15, 'normal'))
btn13.grid(row=3, column=3, sticky='swen', padx=3, pady=3)

btn14 = Button(root, text='+', font=('Comic Sans MS', 15, 'normal'))
btn14.grid(row=4, column=3, sticky='swen', padx=3, pady=3)

btn15 = Button(root, text='.', font=('Comic Sans MS', 15, 'normal'))
btn15.grid(row=4, column=1, sticky='swen', padx=3, pady=3)

btn16 = Button(root, text='=', font=('Comic Sans MS', 15, 'normal'))
btn16.grid(row=4, column=2, sticky='swen', padx=3, pady=3)

# ------------------------------- ВАЖНОЕ -------------------------------

root.mainloop()
