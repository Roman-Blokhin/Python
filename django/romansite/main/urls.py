# Прописываем пути к файлам и функциям

from django.urls import path
from . import views  # 1. импортируем файл с функциями, лежит в этой же папке( . )

# 3. импортируем settings и static, чтобы работал файл локальный со стилями
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),  # 1. пишем путь к функции на главной странице
    path('about', views.about)  # 2. пишем путь к странице about и функции в ней
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 3.1 поможет подключить файл стилей
