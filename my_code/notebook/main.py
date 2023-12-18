from tkinter import *
from tkinter import messagebox


# ---------------------------------- ФУНКЦИИ ----------------------------------

def notebook_exit():  # 1
    answer = messagebox.askokcancel('Выход', 'Вы хотите выйти из программы?')
    if answer:
        root.destroy()


def change_theme(color):
    f_text['bg'] = themes[color]['bg_color']
    f_text['fg'] = themes[color]['fg_color']
    f_text['selectbackground'] = themes[color]['selectbackground_color']
    f_text['insertbackground'] = themes[color]['insertbackground_color']

# ---------------------------------- ОКНО ----------------------------------

root = Tk()
root.title('Блокнот')
root.geometry('750x550+200+200')
root.config(bg='white')
root.resizable(width=True, height=True)
root.iconbitmap(default='logo.ico')
root.protocol('WM_DELETE_WINDOW', notebook_exit)  # выйти, нажав крестик

# ---------------------------------- Словари ----------------------------------

themes = {
    'dark': {
        'bg_color': 'black', 'fg_color': 'lime', 'selectbackground_color': 'LightYellow', 'insertbackground_color':
            'brown',
    },
    'light': {
        'bg_color': 'white', 'fg_color': 'black', 'selectbackground_color': 'grey', 'insertbackground_color': 'black',
    },
    'grey': {
        'bg_color': 'grey', 'fg_color': 'white', 'selectbackground_color': 'pink', 'insertbackground_color': 'black',
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 14 normal'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'normal')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'normal')
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
main_menu = Menu(tearoff=0)  # 1

file_menu = Menu(activeforeground='red')  # 3 -------------------------------
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_command(label='Новое окно')
file_menu.add_separator()
file_menu.add_command(label='Выход', command=notebook_exit)
main_menu.add_cascade(label='Файл', menu=file_menu)

settings_menu = Menu(main_menu)  # 4 -------------------------------

settings_menu_theme = Menu(settings_menu)  # 4.1 theme
settings_menu_theme.add_command(label='Темная')
settings_menu_theme.add_command(label='Светлая')
settings_menu_theme.add_command(label='Серая')
settings_menu.add_cascade(menu=settings_menu_theme, label='Тема')

settings_menu_font = Menu(settings_menu)  # 4.2 fonts
settings_menu_font.add_command(label='Arial')
settings_menu_font.add_command(label='Comic Sans MS')
settings_menu_font.add_command(label='Times New Roman')
settings_menu.add_cascade(menu=settings_menu_font, label='Шрифт')

settings_menu.add_command(label='Курсор')  # 4.3 cursor
settings_menu.add_command(label='Прозрачность')  # 4.4 transparency
main_menu.add_cascade(label='Настройки', menu=settings_menu)

info_menu = Menu()  # 5 -------------------------------
info_menu.add_command(label='Информация')
main_menu.add_cascade(label='Инфо', menu=info_menu)

root.config(menu=main_menu)  # 2

# ---------------------------------- SCROLLBAR ----------------------------------

scroll = Scrollbar(f_text, orient='vertical', command=f_text.yview)
scroll.pack(side=RIGHT, fill=Y)
f_text['yscrollcommand'] = scroll.set  # f_text.config(yscrollcommand=scroll.set)

# ---------------------------------- ВАЖНОЕ ----------------------------------

root.mainloop()
