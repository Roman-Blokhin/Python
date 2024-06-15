from django import template
import dogs.views as views

# 1. Создаем объект класса Library для регистрации новых тегов
register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db