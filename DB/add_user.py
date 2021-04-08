from db import db_session
from models import User

# создание объекта пользователей
user = User(name='Иван Грозный',salary='1200',email='igrozniy@moskva.ru')
user = User(name='Шурик',salary='800',email='shurik@moskva.ru')
db_session.add(user)
db_session.commit()