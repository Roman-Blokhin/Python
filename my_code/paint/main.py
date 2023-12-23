from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image, ImageDraw


def activate_point(event):
    x1, y1 = (event.x - 2), (event.y - 2)  # указываем толщину линий
    x2, y2 = (event.x + 2), (event.y + 2)  # указываем толщину линий
    cv.create_line(x1, y1, x2, y2, fill='black', width=5)  # линия на холсте
    draw.line((x1, y1, x2, y2), fill='black', width=5)  # линия на холсте для сохранения


root = Tk()
root.title('Paint')

root.config(bg='')
root.resizable(width=False, height=False)

cv = Canvas(root, width=800, height=500, bg='white')  # 1. создали канву - холст для рисования

image_1 = PIL.Image.new('RGB', (800, 500), 'white')  # 2. переменная с параметрами изображения(место для рисунка)
draw = PIL.ImageDraw.Draw(image_1)  # 3. инструмент для рисования

cv.bind('<B1-Motion>', activate_point)  # подключили левую кнопку для использования, команды пока нет
cv.pack(expand=1, fill=BOTH)

btn_save = Button(root, text='Сохранить', bg='black', fg='white', font=('Comic Sans MS', 30))
btn_save.pack()

root.mainloop()
