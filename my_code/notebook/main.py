from tkinter import *
from tkinter import messagebox


# ---------------------------------- ФУНКЦИИ ----------------------------------

def notebook_exit():  # 1
    answer = messagebox.askokcancel('Выход', 'Вы хотите выйти из программы?')
    if answer:
        root.destroy()


def change_theme(color):  # 2
    f_text['bg'] = themes[color]['bg_color']
    f_text['fg'] = themes[color]['fg_color']
    f_text['selectbackground'] = themes[color]['selectbackground_color']
    f_text['insertbackground'] = themes[color]['insertbackground_color']
    f_text['selectforeground'] = themes[color]['selectforeground_color']


def change_font(num):
    f_text['font'] = fonts[num]['other_font']


def change_cursor(var):
    f_text['cursor'] = cursors[var]['curs']


def change_transparent_1():
    root.attributes('-alpha', 0.9)


def change_transparent_2():
    root.attributes('-alpha', 0.8)


def change_transparent_3():
    root.attributes('-alpha', 0.7)


def change_transparent_4():
    root.attributes('-alpha', 0.6)


def change_transparent_5():
    root.attributes('-alpha', 0.5)

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
        'bg_color': 'black', 'fg_color': 'lime', 'selectbackground_color': 'Gainsboro', 'insertbackground_color':
            'brown', 'selectforeground_color': 'red',
    },
    'light': {
        'bg_color': 'white', 'fg_color': 'black', 'selectbackground_color': 'grey', 'insertbackground_color':
            'black', 'selectforeground_color': 'white',
    },
    'grey': {
        'bg_color': 'grey', 'fg_color': 'white', 'selectbackground_color': 'pink', 'insertbackground_color': 'black',
        'selectforeground_color': 'black',
    }
}

fonts = {
    'Arial': {
        'other_font': 'Arial 14 normal'
    },
    'CSMS': {
        'other_font': ('Comic Sans MS', 14, 'normal')
    },
    'TNR': {
        'other_font': ('Times New Roman', 14, 'normal')
    }
}

cursors = {
    'star': {
        'curs': 'star'
    },
    'arrow': {
        'curs': 'arrow'
    },
    'umbrella': {
        'curs': 'umbrella'
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
              selectforeground='white',
              cursor='arrow',
              insertbackground='black',
              spacing3=10,
              )
f_text.pack(fill=BOTH, expand=1)

# ---------------------------------- МЕНЮ ----------------------------------

root.option_add('*tearOff', FALSE)  # 6 отключает пунктирную линию в меню
main_menu = Menu()  # 1

file_menu = Menu(font=('Times New Roman', 12))  # 3 -------------------------------

file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_command(label='Новое окно')
file_menu.add_separator()
file_menu.add_command(label='Выход', command=notebook_exit)
main_menu.add_cascade(label='Файл', menu=file_menu)

settings_menu = Menu(main_menu, font=('Times New Roman', 12))  # 4 -------------------------------

settings_menu_theme = Menu(settings_menu, font=('Times New Roman', 12))  # 4.1 theme
settings_menu_theme.add_command(label='Темная', command=lambda: change_theme('dark'))
settings_menu_theme.add_command(label='Светлая', command=lambda: change_theme('light'))
settings_menu_theme.add_command(label='Серая', command=lambda: change_theme('grey'))
settings_menu.add_cascade(menu=settings_menu_theme, label='Тема')

settings_menu_font = Menu(settings_menu, font=('Times New Roman', 12))  # 4.2 fonts
settings_menu_font.add_command(label='Arial', command=lambda : change_font('Arial'))
settings_menu_font.add_command(label='Comic Sans MS', command=lambda : change_font('CSMS'))
settings_menu_font.add_command(label='Times New Roman', command=lambda : change_font('TNR'))
settings_menu.add_cascade(menu=settings_menu_font, label='Шрифт')

settings_menu_cursor = Menu(settings_menu, font=('Times New Roman', 12))  # 4.3 cursor
settings_menu_cursor.add_command(label='Звезда', command=lambda : change_cursor('star'))
settings_menu_cursor.add_command(label='Стрелка', command=lambda : change_cursor('arrow'))
settings_menu_cursor.add_command(label='Зонтик', command=lambda : change_cursor('umbrella'))
settings_menu.add_cascade(menu=settings_menu_cursor, label='Курсор')

settings_menu_shadow = Menu(settings_menu, font=('Times New Roman', 12))  # 4.4 transparency
settings_menu_shadow.add_command(label='10%', command=change_transparent_1)
settings_menu_shadow.add_command(label='20%', command=change_transparent_2)
settings_menu_shadow.add_command(label='30%', command=change_transparent_3)
settings_menu_shadow.add_command(label='40%', command=change_transparent_4)
settings_menu_shadow.add_command(label='50%', command=change_transparent_5)
settings_menu.add_cascade(menu=settings_menu_shadow, label='Прозрачность')

main_menu.add_cascade(label='Настройки', menu=settings_menu)

info_menu = Menu(font=('Times New Roman', 12))  # 5 -------------------------------
info_menu.add_command(label='Информация')
main_menu.add_cascade(label='Инфо', menu=info_menu)

root.config(menu=main_menu)  # 2

# ---------------------------------- SCROLLBAR ----------------------------------

scroll = Scrollbar(f_text, orient='vertical', command=f_text.yview)
scroll.pack(side=RIGHT, fill=Y)
f_text['yscrollcommand'] = scroll.set  # f_text.config(yscrollcommand=scroll.set)

# ---------------------------------- ВАЖНОЕ ----------------------------------

root.mainloop()
