import flet as ft

def main(page: ft.Page):  
    page.title = 'Погода'  
    page.theme_mode = 'dark'  
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  

    def weather_info(event):
        pass

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()


    user_data = ft.TextField(value='Введите город', width=100)
    btn_theme = ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
    text_change_theme = ft.Text('Погодное приложение')

    page.add(
        ft.Row([btn_theme, text_change_theme], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)  