from db import db_session
from models import User

user = User.query.first()
user.salary = 1562189
db_session.commit()