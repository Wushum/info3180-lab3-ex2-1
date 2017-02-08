from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret Key, Shush'
app.config.from_object(__name__)

from app import views

