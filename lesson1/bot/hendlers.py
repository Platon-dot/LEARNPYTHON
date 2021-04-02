import os
import ephem, datetime
from glob import glob
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton # Клавиатура 
from utils import get_smile, play_random_nambers, main_keyboard, is_human

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
    update.message.reply_text(message,
                reply_markup=main_keyboard())


def send_emoji(update, context):
    rick_list = glob('images\\file*.tgs')
    rick_filename = choice(rick_list)
    chat_id = update.effective_chat.id # отправляем фото конкретному пользователю получая от него его текущий id
    context.bot.sendDocument(chat_id=chat_id, document=open(rick_filename, 'rb'), reply_markup=main_keyboard())
    print(rick_filename)

def send_woman(update, context):
    woman_list = glob('images\\woman_*.jpg')
    woman_filename = choice(woman_list)
    chat_id = update.effective_chat.id 
    context.bot.send_photo(chat_id=chat_id, photo=open(woman_filename, 'rb'), reply_markup=main_keyboard())
    print(woman_filename)



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

def check_user_photo(update, context):
    update.message.reply_text("Идет обработка фото")
    os.makedirs("downloads", exist_ok=True) # создаем папку Download. Если ее нет, то создаем
    user_photo = context.bot.getFile(update.message.photo[-1].file_id)   # положим в переменную файл полученного изображения
    file_name = os.path.join("downloads", f"{user_photo.file_id}.jpg") # в зисимости от операционной системы , прописывается правильный путь к папке с таким \ или таким / слешем
    user_photo.download(file_name)
    if is_human(file_name):
        update.message.reply_text("Обнаружена девушка, добавляю в библиотеку")
        new_filename = os.path.join("images", f"woman_{user_photo.file_id}.jpg")  # переименовать и дать новое имя
        os.rename(file_name, new_filename)
    else:
        update.message.reply_text("Нет девченки на фото")
        os.remove(file_name) # стереть из download не нужный файл котому как он не подходит 
        
        