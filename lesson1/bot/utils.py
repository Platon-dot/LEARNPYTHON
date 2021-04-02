import settings
from clarifai.rest import ClarifaiApp
from emoji import emojize
#from pprint import PrettyPrinter
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
    return ReplyKeyboardMarkup([['Сгонять за Риком','Сгонять за девченками'], 
                                [KeyboardButton('Мои координаты', request_location=True)]], resize_keyboard=True)
    

def is_human(file_name):
    app = ClarifaiApp(api_key=settings.CLARIFAI_API_KEY)
    model = app.public_models.general_model
    responce = model.predict_by_filename(file_name, max_concepts=5)
    if responce['status']['code'] == 10000:
        for concept in responce['outputs'][0]['data']['concepts']:
            if concept['name'] == 'woman':
                return True
    return False

if __name__ == "__main__":
    print(is_human("images/human1.jpg"))
    print(is_human("images/human2.jpg"))