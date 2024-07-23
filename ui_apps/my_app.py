import flet as ft

def main(page: ft.Page):
    page.title = 'Мой первый проект'
    page.theme_mode = 'dark'

    text_name_label = ft.Text(value='Введите имя: ', color='green')
    name_enter = ft.TextField('')
    name_label_text = ft.Text('Ваше имя: ')
    name_label = ft.Text('')

    text_age_label = ft.Text(value='Введите возраст: ', color='green')
    age_enter = ft.TextField('')
    age_label_text = ft.Text('Ваше имя: ')
    age_label = ft.Text('')

    def take_name(event):
        name_label.value = name_enter.value
        page.update()

    def take_age(event):
        age_label.value = age_enter.value
        page.update()

    page.add(
        ft.Row(
            [
                text_name_label,
                name_enter,
                name_label_text,
                name_label
            ]
        ),
        ft.Row(
            [
                text_age_label,
                age_enter,
                age_label_text,
                age_label
            ]
        ),
        ft.Row(
            [
                ft.Text(value='Выберите пол: '),
                ft.Text(value='М'),
                ft.Checkbox(value=False),
                ft.Text(value='Ж'),
                ft.Checkbox(value=False)

            ]
        ),
    )

ft.app(target=main)