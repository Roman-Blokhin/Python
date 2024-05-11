#  ОТВЕЧАЕТ ЗА ТЕ МЕТОДЫ, КОТОРЫЕ БУДУТ ВЫЗВАНЫ ПРИ ПЕРЕХОДЕ НА КОНКРЕТНУЮ СТРАНИЦУ

from django.shortcuts import render
from django.http import HttpResponse  # 1. импортируем для написания текста на странице


# 2. создаем функцию для вывода шаблона
def index(request):
    return render(request, 'main/index.html')


# 4. создаем метод для страницы about
def about(request):
    return render(request, 'main/about.html')


# 3. создаем метод для страницы about, указываем аргумент обязательно, HttpResponse - устаревшее, лучше render
# def about(request):
#     return HttpResponse('<h1>Обо мне</h1>')
