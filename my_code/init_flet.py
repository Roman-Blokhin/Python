import flet as ft

def main(page: ft.Page):
    page.title = '...'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = '500'
    page.window_height = '500'
    page.window_left = '800'
    page.window_top = '200'
    
    def info(event):
        page.update()
        pass

    page.add(
        ft.Row([]),
        ft.Row([]),
    )

ft.app(target=main)