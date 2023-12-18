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

root.option_add('*tearOff', FALSE)  # 6 отключает пунктирную линию в меню
main_menu = Menu(tearoff=0) # 1

file_menu = Menu(activeforeground='red') # 3
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_command(label='Новое окно')
file_menu.add_separator()
file_menu.add_command(label='Выход')
main_menu.add_cascade(label='Файл', menu=file_menu)

settings_menu = Menu()  # 4
settings_menu.add_command(label='Тема')
settings_menu.add_command(label='Шрифт')
settings_menu.add_command(label='Курсор')
main_menu.add_cascade(label='Настройки', menu=settings_menu)

info_menu = Menu()  # 5
info_menu.add_command(label='Информация')
main_menu.add_cascade(label='Инфо', menu=info_menu)


root.config(menu=main_menu)  # 2

# ---------------------------------- SCROLLBAR ----------------------------------

scroll = Scrollbar(f_text, orient='vertical', command=f_text.yview)
scroll.pack(side=RIGHT, fill=Y)
f_text['yscrollcommand'] = scroll.set  # f_text.config(yscrollcommand=scroll.set)

# ---------------------------------- ВАЖНОЕ ----------------------------------

root.mainloop ()