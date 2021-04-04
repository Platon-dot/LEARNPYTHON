from sqlalchemy import create_engine
# использование sqlalchemy в декларативном режиме
from sqlalchemy.ext.declarative import declarative_base
# общение с базой данных
from sqlalchemy.orm import scoped_session, sessionmaker 
import settings

# https://api.elephantsql.com/
engine = create_engine(settings.DB_LINK) 
"""
db_session - позволяет отправлять запросы в базу данных
создание сессии для работы с базой данных
"""
db_session = scoped_session(sessionmaker(bind=engine)) 

# модели будут наследоваться от Base
Base = declarative_base()
Base.query = db_session.query_property()


