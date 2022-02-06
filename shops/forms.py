import email
from logging.config import valid_ident
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo, Length , ValidationError
import email_validator 
from shops.models import User
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Это поле обязательно!"), Email('Не правильный email - адрес')])
    password = PasswordField('Пароль', validators=[DataRequired("Это поле обязательно!"), Length(min=8, max=20, message='Пароль должен быть не меньше 8 и не больше 20 символов')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такой email уже существует!')
