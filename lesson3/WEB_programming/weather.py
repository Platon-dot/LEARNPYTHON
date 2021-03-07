import requests

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': '125b75bf32be455891a221013212702', # все эти данные расположены в строке api что нам отдал сервер
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'aqi': 'ru'
    }
    try:
        result = requests.get(weather_url, params=params) 
        result.raise_for_status()
        weather = result.json()  # здесь мы говорим что хотим получать данные в читаемом для Python виде, в строках, словарях и т.д.
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False

if __name__ == '__main__':
    print(weather_by_city('Barcelona,Spain'))
    