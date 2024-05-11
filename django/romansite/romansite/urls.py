# ОТСЛЕЖИВАЕМ РАЗЛИЧНЫЕ URL АДРЕСА, НА КОТОРЫЕ СМОЖЕМ ПЕРЕХОДИТЬ В РАМКАХ ПРОЕКТА

"""
URL configuration for romansite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 1.1 добавляем include, чтобы прописать путь к главному приложению

urlpatterns = [
    path('admin/', admin.site.urls),  # ПУТЬ К ПАНЕЛИ АДМИНИСТРАТОРА
    path('', include('main.urls')),  # 1. прописываем путь на файл из нашего главного приложения
]
