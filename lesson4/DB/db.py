from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker # общение с базой данных
import settings

engine = create_engine(settings.DB_LINK) # https://api.elephantsql.com/
db_session = scoped_session(sessionmaker(bind=engine)) # db_session - позволяет отправлять запросы в базу данных

Base = declarative_base()
Base.query = db_session.query_property()


