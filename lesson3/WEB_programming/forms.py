from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField # имя пользователя, пароль и т.д
from wtforms.validators import DataRequired # модуль для определения что пользователь ввел данные 


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль пользователя", validators=[PasswordField()])
    submit = SubmitField("Отправить")

