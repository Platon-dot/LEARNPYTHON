import logging # импортируем log файл
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # импорт обработчика команд
import settings
import ephem, datetime
from random import randint, choice
from glob import glob
from emoji import emojize

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO) # Теперь, настроим логирование. Будем записывать все сообщения уровня INFO

def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)# говорим что нужно преобразовать иконку смайлика и передать ее в коде
    update.message.reply_text(f"Привет Бро! {context.user_data['emoji']}")
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

# игровая функция
def play_random_nambers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Твое число {user_number}, моё {bot_number}, ты выиграл'
    elif user_number == bot_number:
        message = f'Твое число {user_number}, моё {bot_number}, ничья'
    else: 
        user_number < bot_number
        message = f'Твое число {user_number}, моё {bot_number}, ты проиграл'
    return message

def guess_number(update, context): # игра с пользователем 
    print(context.args)
    
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_nambers(user_number)
        except (TypeError, ValueError):
            message = 'Введи целое число'
    else:
        message = 'Введи число'
    update.message.reply_text(message)

def send_emoji(update, context):
    rick_list = glob('images\\file*.tgs')
    rick_filename = choice(rick_list)
    chat_id = update.effective_chat.id # отправляем фото конкретному пользователю получая от него его текущий id
    context.bot.sendDocument(chat_id=chat_id, document=open(rick_filename, 'rb'))
    print(rick_filename)

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}")
    
def get_smile(user_data):  # функция выбора случайного смайтика из Settings
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    else:
        return user_data['emoji']

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) # даем команду на котрую будет реагировать бот
    dp.add_handler(CommandHandler('planet', user_planet))
    dp.add_handler(CommandHandler('guess', guess_number)) # кнопрки для бота 
    dp.add_handler(CommandHandler('rick', send_emoji))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # эхо сообщения для пользователя
    
    
    logging.info('Бот стартовал')
    mybot.start_polling()  # команда боту начать ходить в telegram за сообщениями
    mybot.idle() # запуск бота, пока его не остановим принудительно

if __name__ == "__main__":
    main()

