from flask_wtf import Form
from models import User
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
                              Email, Length, EqualTo)

def name_exists(form, field):
  if User.select().where(User.username == field.data).exists():
      raise validationError('User with that username already exists.')

def email_exists(form, field):
  if User.select().where(User.username == field.data).exists():
      raise validationError('User with that username already exists.')

class RegistrationForm(Form):
  username = StringField(
    'Username',
    validators=[
      DataRequired(),
      Regexp(
        r'^[a-zA-Z0-9_]+$',
        message=("Username should be one word, letters, numbers,"
                 " and underscores only.")
      ),
      name_exists
    ])
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


