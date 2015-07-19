#!/usr/bin/env python

from app import *
from login import *
from models import *
from views import *

def initialize_database(db_name):
    DATABASE.init(db_name)
    app.config['DATABASE'] = DATABASE 
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

if __name__ == '__main__':
    try:
        app.config['DATABASE'] = DATABASE
        initialize_database('trendlinks.db')
        User.create_user(
            email='trav221@gmail.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass

    HOST = app.config['HOST']
    PORT = app.config['PORT']
    DEBUG = app.config['DEBUG']
    app.run(
        debug=DEBUG,
        host=HOST, 
        port=PORT
    )

