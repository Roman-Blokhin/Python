import flet as ft
import requests

def main(page: ft.Page):  
    page.title = 'Погода'  
    page.theme_mode = 'light'  
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.window_width='500'  
    page.window_height='500'
    page.window_left='800'  
    page.window_top='200'


    def get_info(event):
        if len(user_data.value) <= 2:
            return
        API = 'af76dfe719bf598fba88c3b95130f5d0'  # ключ с сервиса погоды
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'  # ссылка на сервис
        res = requests.get(URL).json()  # используем формат .json для вывода информации
        temp = res['main']['temp']
        weather_deg.value = f'Погода в городе {user_data.value}: ' + str(temp)
        print(res)
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()


    user_data = ft.TextField(label='Введите город', width=200)
    btn_theme = ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
    text_change_theme = ft.Text('Погодное приложение')
    btn_weather = ft.IconButton(ft.icons.PLAY_ARROW_SHARP, on_click=get_info)
    weather_deg = ft.Text('')

    page.add(
        ft.Row([btn_theme, text_change_theme], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_data, btn_weather], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_deg], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)  