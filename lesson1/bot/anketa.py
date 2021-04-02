from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup # испортируем клавиатуру
from telegram.ext import ConversationHandler
from utils import main_keyboard

def anketa_start(update, context):
    update.message.reply_text(
        "Как тебя звать-то? Давайка по Имени и Фамилии", 
        reply_markup=ReplyKeyboardRemove()
)
    return "name"

def anketa_name(update, context):
    user_name = update.message.text # то что вводит пользователь, мы укладываем в переменную 
    if len(user_name.split()) < 2:
        update.message.reply_text("Веди Имя и Фимилию")
        return "name"
    else:
        context.user_data["anketa"] = {"name": user_name}
        reply_keyboard = [["1", "2", "3"], 
                        ["4", "5"]]
        update.message.reply_text(
            'Оцени моего бота от 1 до 5',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, 
            resize_keyboard=True) # полльзователю клавиатура будет показана один раз и после нажатия будет убрана
        )
        return 'raiting'

def anketa_raiting(update, context):
    context.user_data['anketa']['raiting'] = int(update.message.text)
    update.message.reply_text("Оставь комментарий, или нажми /skip чтобы пропустить")
    return 'comment'

def anketa_comment(update, context):
    context.user_data['anketa']['comment'] = update.message.text
    user_text = format_anketa(context.user_data['anketa'])
    update.message.reply_text(user_text, 
        reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def anketa_skip(update, context):
    user_text = format_anketa(context.user_data['anketa'])
    update.message.reply_text(user_text, 
        reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def format_anketa(anketa):
    user_text = f'''<b>Имя Фамилия</b>: {anketa['name']}
<b>Оценка</b>: {anketa['raiting']}
'''
    if 'comment' in anketa:
        user_text += f"\n<b>Комментарий</b>: {anketa['comment']}"
    return user_text
