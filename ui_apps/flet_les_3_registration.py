import flet as ft

def main(page: ft.Page):
    page.title = 'Регистрация'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = '500'
    page.window_height = '500'
    page.window_left = '800'
    page.window_top = '200'
    page.window_resizable = False


    def register(event):
        pass
        

    def validate(event):
        if all([user_name.value, user_pass.value]):
            btn_reg.disabled = False
        page.update()


    user_name = ft.TextField(label='Введите логин', width=200)
    user_pass = ft.TextField(label='Введите пароль', width=200, password=True)
    btn_reg = ft.OutlinedButton(text='Отправить', disabled=True, on_click=register)


    page.add(
        ft.Row([user_name], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_pass], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn_reg], alignment=ft.MainAxisAlignment.CENTER),
    )


ft.app(target=main)