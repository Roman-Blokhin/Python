from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


def index(request):
    # text = render_to_string('dogs/index.html')
    # return HttpResponse(text)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render (request, 'dogs/index.html', context=data)


def show_post(request, post_id):
    return HttpResponseNotFound(f"Отображение статьи с id = {post_id}")


def about(request):
    return render (request, 'dogs/about.html', {'title': 'О сайте', 'menu': menu})


def addpage(request):
    return render (request, 'dogs/addpage.html', {'title': 'Добавление статьи', 'menu': menu})


def contacts(request):
    return render (request, 'dogs/contacts.html', {'title': 'Обратная связь', 'menu': menu})


def login(request):
    return render (request, 'dogs/login.html', {'title': 'Авторизация', 'menu': menu})


def space(request):
    data = {
        'title': 'космическое пространство',
        'menu': menu,
        'float': 12.909,
        'list': ['toy', 3456, True],
        'obj': MyClass(10, 50),
        'set': {1, 4, 6, 7, 1, 89},
        'dict': {'name': 'value_1', 'surname': 'value_2'},
        'url': slugify('The Main Page Down')
    }
    return render (request, 'dogs/space.html', context=data)


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1> <p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1> <p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 3000:
        raise Http404()
    elif year > 2024:
        return redirect('home')
    return HttpResponse(f'<h1>Архив по годам</h1> <p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена =(</h1>')


menu = [
    {'title': 'О сайте', 'page_name': 'about'},
    {'title': 'Добавить статью', 'page_name': 'addpage'},
    {'title': 'Обратная связь', 'page_name': 'contacts'},
    {'title': 'Войти', 'page_name': 'login'},
]


class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


data_db = [
    {'id': 1, 'title': 'Roman the car', 'content': 'Roman bio congratulations', 'is_published': False},
    {'id': 2, 'title': 'Роберт покоряет горы', 'content': 'Это история про очень смышленого и храброго пса, '
    'который осмелился покорить северный Тянь-Шань. Сегодня он отдыхает дома, а завтра взбирается на горные пики...',
    'is_published': True},
    {'id': 3, 'title': 'Выносливость породы', 'content': 'Сегодня поговорим о том, что на самом деле скрывается за '
    'милой мордочкой вашего питомца', 'is_published': True},
]
