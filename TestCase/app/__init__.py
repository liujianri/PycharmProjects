from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .login import auth
app.register_blueprint(auth)

from .TestCase import case
app.register_blueprint(case,url_prefix='/case')