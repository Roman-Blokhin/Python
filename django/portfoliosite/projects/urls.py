from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('vkusvill/', views.vkusvill, name='vkusvill'),
    path('sletat/', views.sletat, name='sletat'),
    path('skills/', views.skills, name='skills'),
]