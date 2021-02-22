import os

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET KEY'] = 'c2d449cb7fec0e2c5efca449a6dcc6a7'

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

@app.route("/register")
def register(): 
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login(): 
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__": 
    app.run(debug=True, port=3000)