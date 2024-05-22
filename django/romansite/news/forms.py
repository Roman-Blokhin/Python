# ФАЙЛ В КОТОРОМ МЫ СОЕДИНЯЕМ ФОРМУ НА САЙТЕ С МОДЕЛЬЮ БАЗЫ ДАННЫХ

from .models import Article
from django.forms import ModelForms

# 1. описываем класс для формы
class ArticleForm(ModelForms):
    class Meta:
        model = Article  # 1.1 определяем модель
        fields = ['title', 'anons', 'full_text', 'date']  # 1.2 названия полей, которые нужны, из файла models.py

