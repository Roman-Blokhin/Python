from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),  # 1. прописываем путь на нашу функцию отображения страницы, будет главной
    path('cats/<int:cat_id>/', views.categories),  # 2. делаем динамическую страницу по числу
    path('cats/<slug:cat_slug>/', views.categories_by_slug),  # 2. делаем динамическую страницу всем символам
]