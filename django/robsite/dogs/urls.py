from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index),  # 1. прописываем путь на нашу функцию отображения страницы, будет главной
    path('cats/<int:cat_id>/', views.categories),  # 2. делаем динамическую страницу по числу
    path('cats/<slug:cat_slug>/', views.categories_by_slug),  # 3. делаем динамическую страницу всем символам
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)  # 4. путь через использование регулярных выражений
    path('archive/<year4:year>/', views.archive)  # 5. прямой путь через использование конвертера
]