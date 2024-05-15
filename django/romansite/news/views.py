from django.shortcuts import render

def news_home(request):
    return render (request, 'main/about.html')  # 1. Можно использовать шаблоны, которые были в другом приложении.