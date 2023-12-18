from tkinter import *

# ---------------------------------- ФУНКЦИИ ----------------------------------



# ---------------------------------- ОКНО ----------------------------------

root = Tk ()
root.title ('Блокнот')
root.geometry ('750x550+200+200')
root.config (bg = 'white')
root.resizable(width=True, height=True)
root.iconbitmap(default='logo.ico')

# ---------------------------------- КОНТЕЙНЕРЫ ----------------------------------

frame_block = Frame(root)
frame_block.pack(fill=BOTH, expand=1)

# ---------------------------------- ТЕКСТОВОЕ ПОЛЕ ----------------------------------

f_text = Text(frame_block,
              bg='white',
              fg='black',
              font=('Comic Sans MS', 14),
              padx=10, pady=10,
              wrap=WORD,
              selectbackground='grey',
              cursor='arrow',
              insertbackground='black')
f_text.pack(fill=BOTH, expand=1)

# ---------------------------------- ВАЖНОЕ ----------------------------------

root.mainloop ()