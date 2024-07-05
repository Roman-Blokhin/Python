from flask import Flask, render_template

# 1. создаем экземпляр класса
app = Flask(__name__)

# 5. создаем список для меню
menu = ['Установка', 'Приложения', 'Обратная связь']

# 3. создаем декоратор для отображения страницы, указываем адрес главной страницы
@app.route("/index")  # 3.1 на одну функцию можно навешивать несколько url адресов
@app.route("/")
def index():
    return render_template ('index.html', title = 'Главная страница', menu=menu) # 3.2 подключаем созданный шаблон и
    # заголовок, а также список меню

# 4. создаем еще одну страницу
@app.route("/about")  # 4.1 указываем адрес url
def about():
    return render_template ('about.html', menu=menu)

# 2. создаем приложение на нашем локальном сайте
if __name__ == '__main__':
    app.run(debug=True)