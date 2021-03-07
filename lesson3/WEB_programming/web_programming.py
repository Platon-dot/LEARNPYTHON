from flask import Flask, render_template # обязательно второй раз писать с большой буквы
from weather import weather_by_city
from python_org_news import get_python_news

app = Flask(__name__) # передаем в переменную Flask приложение и название 

@app.route('/') # декоратор

def index():
    title = "Новости Python"
    weather = weather_by_city('Barcelona,Spain')
    news_list = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

if __name__ == '__main__': # запуск сервера 
    app.run() # запуск нашего приложчения
    
# тянем погоду через api

# pip install requests

