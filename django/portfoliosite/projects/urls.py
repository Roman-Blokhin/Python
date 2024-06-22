from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('vkusvill/', views.vkusvill, name='vkusvill'),
    path('sletat/', views.sletat, name='sletat'),
    path('skills/', views.skills, name='skills'),

    path('support', views.support, name='support'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('b2b/', views.b2b, name='b2b'),
    path('vvsport/', views.vvsport, name='vvsport'),
    path('ai/', views.ai, name='ai'),
]