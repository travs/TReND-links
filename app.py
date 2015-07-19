from flask import Flask, g
from peewee import SqliteDatabase

import os

app = Flask(__name__)

DEBUG = True
PORT = 8000
HOST = 'localhost'
DATABASE = SqliteDatabase('trendlinks.db')
SECRET_KEY = 'sdhfjkbgddf74u4g8gsnrb73wiur3b2jn3UB!U'
SERVER_NAME = 'localhost:{}'.format(PORT)

app.config.update(dict(
    DEBUG=DEBUG,
    PORT=PORT,
    HOST=HOST,
    DATABASE=DATABASE,
    SECRET_KEY=SECRET_KEY,
    SERVER_NAME=SERVER_NAME
))

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = app.config['DATABASE']
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

