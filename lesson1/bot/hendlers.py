from glob import glob
from random import randint, choice
import ephem, datetime
from telegram import ReplyKeyboardMarkup, KeyboardButton # Клавиатура 

from utils import get_smile, play_random_nambers, main_keyboard

def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)# говорим что нужно преобразовать иконку смайлика и передать ее в коде 
    update.message.reply_text(
        f"Привет Бро! {context.user_data['emoji']}", 
        reply_markup=main_keyboard()
        )
    
    # print(update)
    
def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    my_keyboard = ReplyKeyboardMarkup([['Сгонять за Риком']], resize_keyboard=True)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}", 
                        reply_markup=main_keyboard())

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
    context.bot.sendDocument(chat_id=chat_id, document=open(rick_filename, 'rb'), reply_markup=main_keyboard())
    print(rick_filename)



def user_coordinate(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coordinates = update.message.location
    update.message.reply_text(
        f"Твои координаты {coordinates} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )


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