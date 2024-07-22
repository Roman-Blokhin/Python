import flet as ft

def main(page: ft.Page):  # Основная функция + ft.Page - включает подсказки
    page.title = 'Flet App'  # заголовок
    page.theme_mode = 'dark'  # тема
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # вертикальное расположение элементов

    # добавляет на экран элементы 
    page.add(  
        ft.Row(  # добавляет строки
            [
                ft.IconButton(ft.icons.HOME),  # добавили кнопку - иконку домика
                ft.Icon(ft.icons.BACK_HAND)  # добавили иконку - рука
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(  # новая строка
            [
                ft.IconButton(ft.icons.ACCOUNT_BALANCE),  # кнопка-иконка
                ft.Text('Information', color='#fafafa'),  # просто текст
                # текстовое поле, значение, ширина, расп. текста
                ft.TextField('Enter', width=250, text_align=ft.TextAlign.CENTER)  
            ],
        )
    )

ft.app(target=main)  # прописываем какая функция будет запускаться при старте проектр