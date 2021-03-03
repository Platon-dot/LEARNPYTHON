from flask import Flask # обязательно второй раз писать с большой буквы
from weather import weather_by_city

app = Flask(__name__) # передаем в переменную Flask приложение и название 

@app.route('/') # декоратор

def index():
    weather = weather_by_city('Barcelona,Spain')
    return f"Погода: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"

if __name__ == '__main__': # запуск сервера 
    app.run() # запуск нашего приложчения
    
# тянем погоду через api

# pip install requests

