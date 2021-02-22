import logging # импортируем log файл
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # импорт обработчика команд
import settings
import ephem, datetime

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO) # Теперь, настроим логирование. Будем записывать все сообщения уровня INFO

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text("Привет Бро!")
    # print(update)


def user_planet(update, context):
    planet_name = update.message.text.split()[1]
    now = datetime.datetime.now()
    if planet_name == "Mars":
        planet = ephem.Mars(now.strftime("%d/%m/%Y"))
    elif planet_name == "Venus":
        planet = ephem.Venus(now.strftime("%d/%m/%Y"))
    const = ephem.constellation(planet)
    update.message.reply_text(const)
# planet_now = user_planet("Venus")
# print(planet_now)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) # даем команду на котрую будет реагировать бот
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # эхо сообщения для пользователя
    dp.add_handler(CommandHandler('planet', user_planet))
    
    logging.info('Бот стартовал')
    mybot.start_polling()  # команда боту начать ходить в telegram за сообщениями
    mybot.idle() # запуск бота, пока его не остановим принудительно

if __name__ == "__main__":
    main()

