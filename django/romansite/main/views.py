#  ОТВЕЧАЕТ ЗА ТЕ МЕТОДЫ, КОТОРЫЕ БУДУТ ВЫЗВАНЫ ПРИ ПЕРЕХОДЕ НА КОНКРЕТНУЮ СТРАНИЦУ

from django.shortcuts import render
from django.http import HttpResponse  # 1. импортируем для написания текста на странице


# Create your views here.

# 2. создаем функцию для вывода текста на экран, указываем аргумент обязательно
def index(request):
    return HttpResponse('<h1>Проверка работы</h1>')


# 3. создаем метод для страницы about
def about(request):
    return HttpResponse('<h1>Обо мне</h1>')
