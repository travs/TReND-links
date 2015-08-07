from flask import Flask

PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'

app.config['DEBUG'] = True
app.config['PORT']= PORT
app.config['HOST'] = HOST
app.config['SERVER_NAME'] = '{}:{}'.format(HOST, PORT)

