from flask import Flask

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000
#SERVER_NAME = '{}:{}'.format(HOST, PORT)

app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'

app.config['DEBUG'] = DEBUG
app.config['HOST'] = HOST
app.config['PORT'] = PORT
#app.config['SERVER_NAME'] = SERVER_NAME
