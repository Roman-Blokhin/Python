# Прописываем пути к файлам и функциям

from django.urls import path
from . import views  # 1. импортируем файл с функциями, лежит в этой же папке( . )

urlpatterns = [
    path('', views.index)  # 1. пишем путь к функции
]