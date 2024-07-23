import flet as ft

def main(page: ft.Page):
    page.title = 'Мой первый проект'
    page.theme_mode = 'dark'

    text_label = ft.Text(value='Введите имя', color='green')
    name_enter = ft.TextField('')
    name_label_text = ft.Text('Ваше имя: ')
    name_label = ft.Text('')

    def take_name(event):
        name_label.value = name_enter.value
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.MESSAGE),
                text_label,
                name_enter,
                ft.TextButton('Записать имя', on_click=take_name),
                name_label_text,
                name_label
            ]
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.ARCHIVE),
                ft.Text(value='Архив', color='green')
            ]
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.CALENDAR_MONTH),
                ft.Text('Календарь', color='green')
            ]
        )
    )

ft.app(target=main)