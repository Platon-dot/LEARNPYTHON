import logging # импортируем log файл
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # импорт обработчика команд
import settings

from hendlers import (greet_user, talk_to_me, guess_number,
                    send_emoji, user_coordinate, user_planet)

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO) # Теперь, настроим логирование. Будем записывать все сообщения уровня INFO

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) # даем команду на котрую будет реагировать бот
    dp.add_handler(CommandHandler('planet', user_planet))
    dp.add_handler(CommandHandler('guess', guess_number)) # кнопрки для бота 
    dp.add_handler(CommandHandler('rick', send_emoji))
    dp.add_handler(MessageHandler(Filters.regex('^(Сгонять за Риком)$'), send_emoji)) # реакция на текст в чате
    dp.add_handler(MessageHandler(Filters.location, user_coordinate))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # эхо сообщения для пользователя
    
    logging.info('Бот стартовал')
    mybot.start_polling()  # команда боту начать ходить в telegram за сообщениями
    mybot.idle() # запуск бота, пока его не остановим принудительно

if __name__ == "__main__":
    main()

