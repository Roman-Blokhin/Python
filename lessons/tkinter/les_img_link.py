from tkinter import *
import requests  # позволяет работать с HTTP-запросами
from io import BytesIO
from PIL import ImageTk, Image

url = 'http://s1.fotokto.ru/photo/full/426/4264222.jpg'


def load_img():
    response = requests.get(url)  # открывается ссылка на изображение
    if response.status_code != 200:  # если код состояния картинки не равен 200
        lbl['text'] = 'Изображение не найдено' + str(response.status_code)
    else:  # выведется картинка
        # Image.open(BytesIO(response.content)) - кдасс, мы сохраняем изображение в байтах в буфере памяти
        # resize((400, 400) - картинка сжимается до размеров окна
        # Image.LANCZOS - класс сжатия
        image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((400, 400), Image.LANCZOS))

        lbl.config(image=image)  # присваиваем изображение аргументу лейбла
        lbl.image = image


root = Tk()
root.title('')
root.geometry('400x400+200+200')
root.config(bg='')
root.resizable(False, False)

btn = Button(root, text='Установить фон', command=load_img)
btn.pack()

lbl = Label(root)
lbl.pack()

root.mainloop()
