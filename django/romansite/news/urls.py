# Прописываем пути к файлам и функциям

from django.urls import path
from . import views  # 1. импортируем файл с функциями, лежит в этой же папке( . )

urlpatterns = [
    path('', views.news_home, name='news_home'),  # 2. пишем путь к функции к странице с новостями в приложении news
    path('create', views.create, name='create'),  # 3. путь на страницу добавления новой записи через кнопку в меню
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),  # 4. обращаемся к динамической числовой
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),  # 5. обращаемся к динамической
    # числовой ссылке
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')  # 6. ссылка на шаблон по удалению
    # статьи
]
