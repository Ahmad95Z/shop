import email
from logging.config import valid_ident
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo
import email_validator 
from shops.models import User
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Это поле обязательно!'),  Email("Не правильный email!")])
    password = PasswordField('Пароль', validators=[DataRequired('Это поле обязательно!')])
    confirm_password = PasswordField ('Подтвердите пароль',validators=[DataRequired('Это поле обязательно!'), EqualTo('password')])
    submit = SubmitField('Регистрация')


    def validate_email(self, email):
        user = User.query.flter_by(email=email.data).first()
        if user:
            raise ValidationErr('Такой email существует')
