from django import template
import dogs.views as views

# 1. Создаем объект класса Library для регистрации новых тегов
register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('dogs/list_categories.html')
def show_categories():
    cats = views.cats_db
    return ('cats': cats)