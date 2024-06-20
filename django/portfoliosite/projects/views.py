from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'categories': categories_db,
        'menu': menu,
    }
    return render(request, 'projects/index.html', context=data)


def about(request):
    data = {
        'title': 'Обо мне',
        'categories': categories_db,
        'menu': menu,
    }
    return render(request, 'projects/about.html', context=data)


def vkusvill(request):
    data = {
        'title': 'ВкусВилл',
        'categories': categories_db,
        'menu': menu,
    }
    return render(request, 'projects/vkusvill.html', context=data)


def sletat(request):
    data = {
        'title': 'Слетать.ру',
        'categories': categories_db,
        'menu': menu,
    }
    return render(request, 'projects/sletat.html', context=data)


def skills(request):
    data = {
        'title': 'Skills',
        'categories': categories_db,
        'menu': menu,
    }
    return render(request, 'projects/skills.html', context=data)


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
