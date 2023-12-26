from tkinter import *
from googletrans import Translator


def trans():
    text = text_field_1.get('1.0', END)  # получаем введенную информацию из 1 поле
    cmmnd = tranlator.translate(text, dest='en')  # встроенная команда для перевода, язык - английский
    text_field_1.delete('1.0', END)  # 1 поле очищаем
    text_field_2.insert('1.0', cmmnd.text)  # во 2 поле вставляем переведенный текст


root = Tk()
root.title('Переводчик')
root.geometry('500x500+200+200')
root['bg'] = 'black'
root.resizable(width=False, height=False)

tranlator = Translator()  # активируем переводчик, создавая объект импортируемого класса Translator

lbl_1 = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст:')
lbl_1.pack()

text_field_1 = Text(root, bg='white', fg='black', font='Arial 15 bold', width=35, height=5)
text_field_1.pack()

btn_translate = Button(root, text='Перевести', command=trans)
btn_translate.pack()

text_field_2 = Text(root, bg='white', fg='black', font='Arial 15 bold', width=35, height=5)
text_field_2.pack()

root.mainloop()
