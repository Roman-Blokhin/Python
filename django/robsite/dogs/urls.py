from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),  # 1. прописываем путь на нашу функцию отображения страницы, будет главной
    path('cats/<int:cat_id>/', views.categories),  # 2. делаем динамическую страницу
]