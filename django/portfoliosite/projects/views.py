from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'categories': categories_db,
        'menu': menu,
    }
    return render(request, 'projects/index.html', context=data)


def about(request):
    return render(request, 'projects/about.html')


categories_db = [
    {'id': 1, 'name': 'Служба поддержки'},
    {'id': 2, 'name': 'Лаборатория инноваций'},
    {'id': 3, 'name': 'Международный аудит'},
    {'id': 4, 'name': 'ВкусВилл спорт'},
    {'id': 5, 'name': 'Обучение AI'},
]

menu = [
    {'title': 'ВкусВилл', 'page_name': 'vkusvill'},
    {'title': 'Слетать.ру', 'page_name': 'sletat'},
    {'title': 'Мои скилы', 'page_name': 'skills'},
]
