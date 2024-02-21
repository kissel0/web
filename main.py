from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def func():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(lst)


@app.route('/image_mars')
def image():
    return f'''<title>Привет, Марс!</title>
    <h1>Жди нас, Марс!<h1>
    <img src="{url_for('static', filename='img/mars1.png')}">
    <p><h4>Вот она какая, красивая планета<h4><p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
