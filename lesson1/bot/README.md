# Проект LearnBot 

LearnBot - это бот для Telegram, созданный с целью обучения, который может.
- Высылать место положение планеты
- Высылать emoji Рик и Морти
- Поиграть с тобой в цифры
- Повторить за тобой введенный текст 

## Установка

1. Конфигурируй репозиторий с github
2. Создай виртуальное окружение
3. Установи зависимости 'pip install -r requirements.txt'
4. Создай файл settings.py
5. Впиши в settings.py переменные: 
'''
API_KEY = 'API-ключ бота' 
USER_EMOJI = [':cat2:', ':dragon:',':turtle:', ':panda_face:',':racehorse:', ':elephant:',':camel:', ':horse:',
    ':bug:', ':ant:', ':snail:',':whale:', ':dolphin:',':crocodile:'] 
       #https://www.webfx.com/toolsemoji-cheat-sheet/
'''
6. Запиши бота командой 'python learn_bot.py'