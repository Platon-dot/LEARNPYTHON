import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_python_news(): # функция обработки скачанной html страницы
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts menu') # осуществление поиска. Находит ul на странице
        all_news = all_news.find_all('li') # либо перенести в предыдущую строку all_news = soup.find('ul', class_='list-recent-posts menu').findAll('li')
        result_news = [] #создаем список
        for news in all_news:
            title = news.find('a').text # берем название 
            url = news.find('a')['href'] # берем ссылку
            published = news.find('time').text #забираем дату публикации
            result_news.append({# Укладываем то что получилось в словарь
                "title": title,
                "url": url,
                "published": published
            })
        return result_news
    return False
        # print(title)
        # print(url)
        # print(published)
    
#if __name__ == '__main__':

        #print(news)
        # with open('python.org.html', 'w', encoding='utf-8') as f:  # для сохранения инфы в файл для предварительного анализа
            # f.write(html)
