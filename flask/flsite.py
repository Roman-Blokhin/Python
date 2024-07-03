from flask import Flask

# 1. создаем экземпляр класса
app = Flask(__name__)

# 3. создаем декоратор для отображения страницы, указываем адрес главной страницы
@app.route("/")
def index():
    return 'Main page'

# 2. создаем приложение на нашем локальном сайте
if __name__ == '__main__':
    app.run(debug=True)