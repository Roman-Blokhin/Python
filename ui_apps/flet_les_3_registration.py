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
        

    def validate(event):  # условие об активации кнопки Отправить
        if all([user_name.value, user_pass.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page.update()


    user_name = ft.TextField(label='Введите логин', width=200, on_change=validate)  # on_change - проверят заполненность полей
    user_pass = ft.TextField(label='Введите пароль', width=200, password=True, on_change=validate)
    btn_reg = ft.OutlinedButton(text='Отправить', disabled=True, on_click=register)


    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Регистрация:'),
                        user_name,
                        user_pass,
                        btn_reg
                    ]
                )
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)