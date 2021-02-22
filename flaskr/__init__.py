from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# APP CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2d449cb7fec0e2c5efca449a6dcc6a7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# ROUTES 
from flaskr import routes

