import settings
from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton # Клавиатура 



def get_smile(user_data):  # функция выбора случайного смайтика из Settings
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    else:
        return user_data['emoji']

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


def main_keyboard():
    return ReplyKeyboardMarkup([['Сгонять за Риком', KeyboardButton('Мои координаты', request_location=True)]], resize_keyboard=True)


