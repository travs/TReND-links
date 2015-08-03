from flask.ext.wtf import Form
from models import User
from wtforms import DateField, StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
        Email, Length, EqualTo)

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')

class RegistrationForm(Form):
    email = StringField(
    'Email',
    validators=[
        DataRequired(),
        Email(),
        email_exists
    ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class ProfileForm(Form):
    name = StringField('Name')
    country = StringField('Country')
    birthdate = DateField('Birthday')
