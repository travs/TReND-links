from flask import Flask, g
from peewee import SqliteDatabase
import os

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

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

