import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

def get_db(db_name):
    return SqliteDatabase(db_name)

DATABASE = get_db('trendlinks.db')

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, email, password, admin=False):
        try:
            cls.create(
                email=email,
                password=generate_password_hash(password),
                is_admin=admin
            )
        except IntegrityError:
            raise ValueError("User already exists")

class UserProfile(Model):
    user = ForeignKeyField(User, related_name="profile")
    name = CharField(max_length=50)
    age = DateField()
    country = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user_profile(cls, user, name, age, country):
        try:
            cls.create(
                user=user,
                name=name,
                age=age,
                country=country
            )
        except IntegrityError:
            raise ValueError("Profile already exists for this user")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

