import flet as ft

def main(page: ft.Page):
    page.title = 'Мой первый проект'
    page.theme_mode = 'dark'

    text_name_label = ft.Text(value='Введите имя: ', color='red')
    text_age_label = ft.Text(value='Введите возраст: ', color='red')

    name_enter = ft.TextField(hint_text='Введите текст', text_align=ft.TextAlign.RIGHT)  # hint_text - пример текста
    age_enter = ft.TextField(label='Введите текст', text_align=ft.TextAlign.RIGHT)  # label - красивая анимация надписи
    
    name_label_text = ft.Text('Ваше имя: ')
    name_label = ft.Text('')

    age_label_text = ft.Text('Ваш возраст: ')
    age_label = ft.Text('')

    gender_label_text = ft.Text('Ваш пол: ')
    gender_label = ft.Text('')


    def take_info(event):
        name_label.value = name_enter.value
        age_label.value = age_enter.value
        # name_enter.focus()  # устанавливает фокус на поле ввода
        page.update()


    page.add(
        ft.Row(
            [
                text_name_label,
                name_enter,
                name_label
            ]
        ),
        ft.Row(
            [
                text_age_label,
                age_enter,
                age_label
            ]
        ),
        ft.Row(
            [
                ft.Text(value='Выберите пол: ', color='red'),
                ft.Text(value='М'),
                ft.Checkbox(value=False),
                ft.Text(value='Ж'),
                ft.Checkbox(value=False)
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton('Отправить', on_click=take_info),
            ]
        ),
        ft.Row(
            [
                name_label_text,
                name_label,
            ]
        ),
        ft.Row(
            [
                age_label_text,
                age_label
            ]
        ),
        ft.Row(
            [
                gender_label_text,
                gender_label,
            ]
        )
    )

ft.app(target=main)