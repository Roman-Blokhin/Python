import flet as ft

def main(page: ft.Page):
    page.title = 'Выпадающий список'
    page.window_width='500'
    page.window_height='500'
    page.window_left='800'
    page.window_top='200'
    page.bgcolor=ft.colors.WHITE
    

    def clicked_btn(event):
        if color_dropdown.value == 'red':
            text.value = f'Вы выбрали цвет: {color_dropdown.value}'
            page.bgcolor=ft.colors.RED_300
        elif color_dropdown.value == 'green':
            text.value = f'Вы выбрали цвет: {color_dropdown.value}'
            page.bgcolor=ft.colors.GREEN_700
        elif color_dropdown.value == 'grey':
            text.value = f'Вы выбрали цвет: {color_dropdown.value}'
            page.bgcolor=ft.colors.GREY_300
        else:
            text.value = f'Вы не выбрали цвет'
            page.bgcolor=ft.colors.WHITE 
        page.update()

    btn = ft.OutlinedButton('Отправить', on_click=clicked_btn)
    text = ft.Text ()
    color_dropdown = ft.Dropdown (
        width=100,
        options=[
            ft.dropdown.Option('red'),
            ft.dropdown.Option('green'),
            ft.dropdown.Option('grey'),
        ]
    )

    page.add(color_dropdown, btn, text)

ft.app(target=main)    