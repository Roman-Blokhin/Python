from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='home'),  # 1. прописываем путь на нашу функцию отображения страницы, будет главной
    path('about/', views.about, name='about'),
    path('space/', views.space, name='space'),
    path('post/<int:post_id>/', views.show_post, name='post'),  # 6. путь на динамические страницы со статьями

    path('cats/<int:cat_id>/', views.categories, name='cats_id'),  # 2. делаем динамическую страницу по числу
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # 3. делаем динамическую стр. всем символам
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)  # 4. путь через использование регулярных выражений
    path('archive/<year4:year>/', views.archive, name='archive')  # 5. прямой путь через использование конвертера
]