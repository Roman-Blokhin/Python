# ФАЙЛ В КОТОРОМ МЫ СОЕДИНЯЕМ ФОРМУ НА САЙТЕ С МОДЕЛЬЮ БАЗЫ ДАННЫХ

from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

# 1. описываем класс для формы
class ArticleForm(ModelForm):
    class Meta:
        model = Article  # 1.1 определяем модель
        fields = ['title', 'anons', 'full_text', 'date']  # 1.2 названия полей, которые нужны, из файла models.py

        # 2. прописываем виджеты для нашей формы
        widgets = {
            'title': TextInput({
                'class': 'form-control',
                'placeholder': "Article's name"
            }),
            'anons': TextInput({
                'class': 'form-control',
                'placeholder': "Article's notification"
            }),
            'full_text': Textarea({
                'class': 'form-control',
                'placeholder': "Atricle's text"
            }),
            'date': DateTimeInput({
                'class': 'form-control',
                'placeholder': "Date of public"
            }),
        }

