import datetime
from app import app
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(None)

def initialize(db_name):
    DATABASE.init(db_name)
    DATABASE.connect()
    DATABASE.create_tables([User, UserProfile], safe=True)
    DATABASE.close()

class User(UserMixin, Model):
    email = CharField(unique=True)
    nickname = CharField(unique=True, null=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)
    confirmed = BooleanField(default=True)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, email, password, admin=False, confirmed=True):
        try:
            cls.create(
                email=email,
                password=generate_password_hash(password),
                is_admin=admin,
                confirmed=confirmed,
            )
        except IntegrityError:
            raise ValueError('User already exists')

class UserProfile(Model):
    user = ForeignKeyField(User, related_name='profile', unique=True)
    name = CharField(max_length=50, null=True)
    birthdate = DateField(null=True)
    country = CharField(max_length=100, null=True)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user_profile(cls, user):
        try:
            cls.create(
                user=user,
            )
        except IntegrityError:
            raise ValueError('Profile already exists for this user')

