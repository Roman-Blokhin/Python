# Прописываем пути к файлам и функциям

from django.urls import path
from . import views  # 1. импортируем файл с функциями, лежит в этой же папке( . )

urlpatterns = [
    path('', views.news_home, name= 'news_home'),  # 2. пишем путь к функции к странице с новостями в приложении news
]
