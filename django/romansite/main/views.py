#  ОТВЕЧАЕТ ЗА ТЕ МЕТОДЫ, КОТОРЫЕ БУДУТ ВЫЗВАНЫ ПРИ ПЕРЕХОДЕ НА КОНКРЕТНУЮ СТРАНИЦУ

from django.shortcuts import render
from django.http import HttpResponse  # 1. импортируем для написания текста на странице


# 2. создаем функцию для вывода шаблона
def index(request):
    return render(request, 'main/index.html')


# 4. создаем метод для страницы about
def about(request):
    return render(request, 'main/about.html')


# 5. создаем метод для страницы about
def contacts(request):
    return render(request, 'main/contacts.html')


# 6. создаем метод для страницы space, где будем тестировать различные фичи
# третим параметром передается словарь, по ключу которого значение передается в html файл
# можно передавать просто 1 ключ/значение - {'title': 'Space'}, но лучше отдельно в методе создать словарь
def space(request):
    data = {
        'title': 'Space',
        'values': ['123', 'name', 'car'],
        'elements': ['microsoft', 'apple', 'facebook'],
        'colors': {
            'green': 'tree',
            'yellow': 'sun',
            'black': 'night',
        }
    }
    return render(request, 'main/space.html', data)



# ------------------------------------------------------------------ #
# 3. создаем метод для страницы about, указываем аргумент обязательно, HttpResponse - устаревшее, лучше render
# def about(request):
#     return HttpResponse('<h1>Обо мне</h1>')
