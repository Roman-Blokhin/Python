from tkinter import *
from googletrans import Translator


def trans():
    text = text_field_1.get('1.0', END)
    cmmnd = tranlator.translate(text, dest='en')
    text_field_1.delete('1.0', END)
    text_field_2.insert('1.0', cmmnd.text)

root = Tk ()
root.title ('Переводчик')
root.geometry ('500x500+200+200')
root['bg'] = 'black'
root.resizable(width=False, height=False)

tranlator = Translator()

lbl_1 = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст:')
lbl_1.pack()

text_field_1 = Text(root, bg='white', fg='black', font='Arial 15 bold', width=35, height=5)
text_field_1.pack()

btn_translate = Button(root, text='Перевести', command=trans)
btn_translate.pack()

text_field_2 = Text(root, bg='white', fg='black', font='Arial 15 bold', width=35, height=5)
text_field_2.pack()

root.mainloop ()