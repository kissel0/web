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
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body><link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                    <h1>Жди нас, Марс!<h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/choice/<planet_name>')
def option(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение:{planet_name}</h1>
                        <h2>Эта планета близка к Земле;</h2>
                        <div class="alert alert-success" role="alert">
                            На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-warning" role="alert">
                            На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Наконец, она просто красива!;
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Пример с несколькими параметрами</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}:</h2>
                        <div class="alert alert-success" role="alert">
                            <h2>Поздравляем! Ваш рейтинг после {level} этапа отбора</h2>
                        </div>
                        <h4>составляет {rating}!</h4>
                        <div class="alert alert-warning" role="alert">
                            <h2>Желаем удачи!</h2>
                        </div>
                      </body>
                    </html>'''


@app.route('/image_mars')
def image():
    return f'''<title>Привет, Марс!</title>
    <h1>Жди нас, Марс!<h1>
    <img src="{url_for('static', filename='img/mars.png')}">
    <p><h4>Вот она какая, красивая планета<h4><p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
