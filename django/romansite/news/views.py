from django.shortcuts import render
from .models import Article  # 2 импортируем табличку Article
from .forms import ArticleForm  # 3.2 импортируем класс формы

def news_home(request):
    # news = Article.objects.all()  # 2.1 переменная, которая принимает на себя все объекты таблицы Article
    # news = Article.objects.order_by('-title')  # 2.3 сортировка статей по возрастанию
    # news = Article.objects.order_by('title')  # 2.2 сортировка статей по убыванию
    news = Article.objects.order_by('-date') [:2]  # 2.2 сортировка по дате публикации, срез - 2 записи

    return render (request, 'news/news_home.html', {'news': news})
    # 1. Можно использовать шаблоны, которые были в другом приложении.
    # 2.2 Третьим параметром передаем news в виде ключ: значение


# 3.1 создали функцию для открытия страницы, где можно добавить новую статью
def create(request):
    error = ''  # 4.5 создаем переменную для вывода текста с ошибкой
    # 4. прописываем получение данных из формы, показ ошибок, обработку, перенаправление на новую страницу
    if request.method == 'POST':  # 4.1 проверяем метод передачи данных со страницы формы
        form = ArticleForm(request.POST)  # 4.2 здесь будут храниться все данные, полученные из формы
        if form.is_valid():  # 4.3 проверяем, корректные ли данные
            form.save()  # 4.4 если да, то мы их сохраняем в БД
        else:
            error = 'Form is uncorrected'  # 4.6 если нет, выводим текст ошибки

    # 3.3 создание объекта
    form = ArticleForm()

    date = {  # 3.4 создание словаря, куда передаем объект класса
        'form': form,
        'error': error  # 4.7 добавляем текст ошибки
    }
    return render (request, 'news/create.html', date)  # 3.5 передаем словарь, как аргумент
