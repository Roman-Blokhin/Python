import flet as ft

def main(page: ft.Page):  # Основная функция + ft.Page - включает подсказки
    page.title = 'Flet App'  # заголовок
    page.theme_mode = 'dark'  # тема
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # вертикальное расположение элементов


    user_label = ft.Text('Info', color='#fafafa')  # просто текст
    # текстовое поле, значение, ширина, расп. текста
    user_text = ft.TextField('Enter', width=250, text_align=ft.TextAlign.CENTER)

    # функция, которая берет наше значение из текстового поля и передает его в отображаемый текст
    def get_info(enter):
        user_label.value = user_text.value
        page.update()  # обязательное обновление экрана

    
    page.add(  # добавляет на экран элементы 
        ft.Row(  # добавляет строку
            [
                ft.IconButton(ft.icons.HOME, on_click=get_info),  # добавили кнопку - иконку домика, принимает функцию
                ft.Icon(ft.icons.BACK_HAND)  # добавили иконку - рука
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(  # новая строка
            [
                user_label,
                user_text
            ],
        )
    )

# прописываем какая функция будет запускаться при старте проекта
ft.app(target=main)  # если ввести - view=ft.AppView.WEB_BROWSER, то приложение отобразится в браузере