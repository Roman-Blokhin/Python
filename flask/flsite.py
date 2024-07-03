from flask import Flask

# 1. создаем экземпляр класса
app = Flask(__name__)

# 3. создаем декоратор для отображения страницы, указываем адрес главной страницы
@app.route("/")
def index():
    return 'Main page'

# 3. создаем еще одну страницу
@app.route("/about")  # 3.1 указываем адрес url
def about():
    return '<h1>About Company</h1>'

# 2. создаем приложение на нашем локальном сайте
if __name__ == '__main__':
    app.run(debug=True)