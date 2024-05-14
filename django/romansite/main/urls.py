# Прописываем пути к файлам и функциям

from django.urls import path
from . import views  # 1. импортируем файл с функциями, лежит в этой же папке( . )

urlpatterns = [
    path('', views.index, name= 'home'),  # 1. пишем путь к функции на главной странице
    path('about', views.about, name= 'about'),  # 2. пишем путь к странице about и функции в ней
    path('contacts', views.contacts, name= 'contacts'),
    path('space', views.space, name= 'space'),
]
