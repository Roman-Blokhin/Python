from django.shortcuts import render
from .models import Article  # 2 импортируем табличку Article

def news_home(request):
    news = Article.objects.all()  # 2.1 переменная, которая принимает на себя все объекты таблицы Article
    return render (request, 'news/news_home.html', {'news': news})
    # 1. Можно использовать шаблоны, которые были в другом приложении. 3им параметром передаем news
