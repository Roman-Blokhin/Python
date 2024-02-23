from tkinter import *

# ------------------------------- ФУНКЦИИ -------------------------------

def first():
    pass


# ------------------------------- ОКНО -------------------------------

root = Tk()
root.title('Калькулятор')
root.geometry('400x400+200+200')
root.config(bg='Grey')
root.resizable(False, False)

# ------------------------------- ОКНО ВЫВОДА -------------------------------

entry = Entry(root, width=15, font=('Comic Sans MS', 15, 'bold'))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ------------------------------- КНОПКИ -------------------------------

btn1 = Button(root, text='1', font=('Comic Sans MS', 15, 'bold'))
btn1.grid(row=1, column=0, sticky='swen', padx=3, pady=3)

btn2 = Button(root, text='2', font=('Comic Sans MS', 15, 'bold'))
btn2.grid(row=1, column=1, sticky='swen', padx=3, pady=3)

btn3 = Button(root, text='3', font=('Comic Sans MS', 15, 'bold'))
btn3.grid(row=1, column=2, sticky='swen', padx=3, pady=3)

btn4 = Button(root, text='4', font=('Comic Sans MS', 15, 'bold'))
btn4.grid(row=2, column=0, sticky='swen', padx=3, pady=3)

btn5 = Button(root, text='5', font=('Comic Sans MS', 15, 'bold'))
btn5.grid(row=2, column=1, sticky='swen', padx=3, pady=3)

btn6 = Button(root, text='6', font=('Comic Sans MS', 15, 'bold'))
btn6.grid(row=2, column=2, sticky='swen', padx=3, pady=3)

btn7 = Button(root, text='7', font=('Comic Sans MS', 15, 'bold'))
btn7.grid(row=3, column=0, sticky='swen', padx=3, pady=3)

btn8 = Button(root, text='8', font=('Comic Sans MS', 15, 'bold'))
btn8.grid(row=3, column=1, sticky='swen', padx=3, pady=3)

btn9 = Button(root, text='9', font=('Comic Sans MS', 15, 'bold'))
btn9.grid(row=3, column=2, sticky='swen', padx=3, pady=3)

btn0 = Button(root, text='0', font=('Comic Sans MS', 15, 'bold'))
btn0.grid(row=4, column=0, sticky='swen', padx=3, pady=3)

# ------------------------------- ВАЖНОЕ -------------------------------

root.mainloop()
