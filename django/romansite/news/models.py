# СОЗДАЕМ БАЗУ ДАНННЫХ

from django.db import models


class Article(models.Model):  # 1. создаем класс для базы данных
    # 2. нужно каждую колонку обозначить типом данных, написать название, добавить параметры
    title = models.CharField('Title',  max_length=50)  # 2.1 строка до 250 символов
    anons = models.CharField('Notification',  max_length=250)
    full_text = models.TextField('Article')  # 2.2 строка больше 250 символов
    date = models.DateTimeField('Дата публикации')  # 2.3 дата и время

    def __str__(self):
        return self.title

    # 3 создаем класс, в которой мы укажем названия для нашей таблицы в ед. и мн. числе
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


