import flet as ft

def main(page: ft.Page):
    page.title = 'Изучаю новые функции самостоятельно'
    page.theme_mode = 'dark'

    true = 'Выполнено'
    false = 'Не выполнено'

    def check_1_clicked(e):
        if check_1.value == True:
            output_text.value = f'Статус задачи: {true}'
        else:
            output_text.value = f'Статус задачи: {false}'
        page.update()

    output_text = ft.Text()
    check_1 = ft.Checkbox(label='ToDo: go to work', value=False)
    btn_1 = ft.ElevatedButton('Отправить данные', on_click=check_1_clicked)

    page.add(check_1, btn_1, output_text)

ft.app(target=main)