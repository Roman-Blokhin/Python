from django.shortcuts import render
from .models import Article  # 2 импортируем табличку Article

def news_home(request):
    # news = Article.objects.all()  # 2.1 переменная, которая принимает на себя все объекты таблицы Article
    # news = Article.objects.order_by('-title')  # 2.3 сортировка статей по возрастанию
    # news = Article.objects.order_by('title')  # 2.2 сортировка статей по убыванию
    news = Article.objects.order_by('-date') [:2]  # 2.2 сортировка по дате публикации, срез - 2 записи

    return render (request, 'news/news_home.html', {'news': news})
    # 1. Можно использовать шаблоны, которые были в другом приложении.
    # 2.2 Третьим параметром передаем news в виде ключ: значение


# 3. создали функцию для открытия страницы, где можно добавить новую статью
def create(request):
    return render (request, 'news/create.html')
