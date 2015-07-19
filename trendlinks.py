#!/usr/bin/env python

from app import app
from login import *
from models import *
from views import *

DATABASE = app.config['DATABASE']
HOST = app.config['HOST']
PORT = app.config['PORT']
DEBUG = app.config['DEBUG']

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

if __name__ == '__main__':
    try:
        initialize()
        User.create_user(
            email='trav221@gmail.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass
    app.run(
        debug=DEBUG,
        host=HOST, 
        port=PORT
    )

