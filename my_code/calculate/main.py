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

# ------------------------------- ВАЖНОЕ -------------------------------

root.mainloop()
