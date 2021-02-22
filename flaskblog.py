import os

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import RegistrationForm, LoginForm

# APP CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2d449cb7fec0e2c5efca449a6dcc6a7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# USER MODEL 
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self): 
        return f"User({self.id}): {self.username}, {self.image_file}"

# POST MODEL
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self): 
        return f"Post({self.id}): {self.title}, {self.date_posted}"

posts = [
    {
        "author": "Derek Oshita", 
        "title": "Freakin blog dude", 
        "content": "First content", 
        "date_posted": "April 14, 1992"

    }, 
        {
        "author": "Mila Oshita", 
        "title": "Best lady", 
        "content": "Second content", 
        "date_posted": "April 20, 1992"
    }
]

@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html", posts=posts)

@app.route("/about")
def about(): 
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit(): 
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password': 
            flash(f"You have been logged in!", 'success') 
            return redirect(url_for('home'))
        else: 
            flash(f"Login unsuccessful. Please check credentials.", "danger")
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__": 
    app.run(debug=True, port=3000)