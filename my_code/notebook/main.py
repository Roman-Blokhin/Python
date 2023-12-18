from tkinter import *

# ---------------------------------- ФУНКЦИИ ----------------------------------



# ---------------------------------- ОКНО ----------------------------------

root = Tk ()
root.title ('Блокнот')
root.geometry ('750x550+200+200')
root.config (bg = 'white')
root.resizable(width=True, height=True)
root.iconbitmap(default='logo.ico')

# ---------------------------------- Словари ----------------------------------

themes = {
    'dark': {
        'bg': 'black', 'fg': 'lime', 'selectbackground': 'LightYellow', 'insertbackground': 'brown',
    },
    'light': {
        'bg': 'white', 'fg': 'black', 'selectbackground': 'grey', 'insertbackground': 'black',
    },
    'grey': {
        'bg': 'grey', 'fg': 'white', 'selectbackground': 'pink', 'insertbackground': 'black',
    }
}

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
              insertbackground='black',
              spacing3=10,
              width=30)
f_text.pack(fill=BOTH, expand=1)

# ---------------------------------- МЕНЮ ----------------------------------

main_menu = Menu()

main_menu.add_cascade(label='Файл')
main_menu.add_cascade(label='Настройки')
main_menu.add_cascade(label='Инфо')

root.config(menu=main_menu)

# ---------------------------------- SCROLLBAR ----------------------------------

scroll = Scrollbar(f_text, orient='vertical', command=f_text.yview)
scroll.pack(side=RIGHT, fill=Y)
f_text['yscrollcommand'] = scroll.set  # f_text.config(yscrollcommand=scroll.set)

# ---------------------------------- ВАЖНОЕ ----------------------------------

root.mainloop ()