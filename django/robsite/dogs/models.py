from django.db import models

# 1. Создаем класс для создания базы данных
class Dogs(models.Model):
    title = models.CharField(max_length=255)  # 2. текстовое поле, длина 255 символов
    content = models.TextField(blank=True)  # 3. большое текстовое поле, необязательно для заполнения(blank)
    time_create = models.DateTimeField(auto_now_add=True)  # 4. время создания записи, заполняется автоматически
    time_update = models.DateTimeField(auto_now=True)  # 5. время изменения записи, заполняется автоматически
    is_published = models.BooleanField(default=True)  # 6. автоматом проставляется, что статья опубликована
