import flet as ft

def main(page: ft.Page):
    page.title = '...'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = '500'
    page.window_height = '500'
    page.window_left = '800'
    page.window_top = '200'
    page.window_resizable = False
    
    def info(event):
        page.update()
        pass

    page.add(
        ft.Row([], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([], alignment=ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)