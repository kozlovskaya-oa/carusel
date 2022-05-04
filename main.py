from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ["Человечество вырастает из детства.",
           "Человечеству мала одна планета.",
           "Мы сделаем обитаемыми безжизненные пока планеты.",
           "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(lst)


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Жди нас Марс</title>
                  </head>
                  <body>
                    <h1>Жди нас Марс</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    <h1>Вот она какая, красная планета</h1>
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Пейзажи Марса</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
  <h2>Пейзажи Марса</h2>  
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
      <div class="item active">
        <img src="{url_for('static', filename='img/slide_1.jpg')}" alt="image 1" style="width:100%;">
      </div>

      <div class="item">
        <img src="{url_for('static', filename='img/slide_2.jpg')}" alt="image 2" style="width:100%;">
      </div>
    
      <div class="item">
        <img src="{url_for('static', filename='img/slide_3.jpg')}" alt="image 3" style="width:100%;">
      </div>
    </div>
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
