import os
from peewee import SqliteDatabase

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'wanna-go-for-an-override?'
#    HOST = '0.0.0.0'
#    PORT = 5000
    DATABASE = SqliteDatabase(None)


class ProductionConfig(Config):
    DEBUG = True
#    PORT = int(os.environ.get('PORT'))
#    SERVER_NAME = '{}:{}'.format(Config.HOST, PORT)


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    SECRET_KEY = 'sdhfjkbgddf74u4g8gsnrb73wiur3b2jn3UB!U'
    DEVELOPMENT = True
    DEBUG = True
#    HOST = 'localhost'
#    SERVER_NAME = '{}:{}'.format(HOST, Config.PORT)



class TestingConfig(Config):
    TESTING = True
    CSRF_ENABLED = False

