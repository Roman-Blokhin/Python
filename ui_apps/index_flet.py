import flet as ft

def main(page: ft.Page):  # Основная функция + ft.Page - включает подсказки
    page.title = 'Flet App'  # заголовок
    page.theme_mode = 'dark'  # тема

ft.app(target=main)  # прописываем какая функция будет запускаться при старте проект