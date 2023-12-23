from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image, ImageDraw

root = Tk ()
root.title ('Paint')
root.config (bg = '')
root.resizable(width=False, height=False)

cv = Canvas(root, width=1280, height=720, bg='white')  # 1. создали канву - холст для рисования

image_1 = PIL.Image.new('RGB', (1280, 720), 'white')  # 2. переменная с параметрами изображения(место для рисунка)
draw = PIL.ImageDraw.Draw(image_1)  # 3. инструмент для рисования


root.mainloop ()