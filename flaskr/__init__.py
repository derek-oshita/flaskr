from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# APP CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2d449cb7fec0e2c5efca449a6dcc6a7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# ROUTES 
from flaskr import routes

