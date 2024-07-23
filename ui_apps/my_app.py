import flet as ft

def main(page: ft.Page):
    page.title = 'Мой первый проект'
    page.theme_mode = 'dark'

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.MESSAGE),
                ft.Text('Создать запись')
            ]
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.ARCHIVE),
                ft.Text('Архив')
            ]
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.CALENDAR_MONTH),
                ft.Text('Календарь')
            ]
        )
    )

ft.app(target=main)