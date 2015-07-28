#!/usr/bin/env python

import os, subprocess
from app import *
from login import *
from models import *
from views import *

def initialize_database(db_name):
    app.config['DATABASE'] = DATABASE
    DATABASE.init(db_name)
    DATABASE.connect()
    DATABASE.create_tables([User, UserProfile], safe=True)
    DATABASE.close()

initialize_database('trendlinks.db')

if __name__ == '__main__':
    if not os.name == 'nt':
        subprocess.call(['gunicorn', 'trendlinks:app', '-b', '0.0.0.0:5000'])
    else:
        try:
            initialize_database('trendlinks.db')
        except ValueError:
            pass
        else:
            app.run()
