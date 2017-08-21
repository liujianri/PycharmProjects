from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import longLive_serves
from app import set_meu
