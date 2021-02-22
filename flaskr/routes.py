from flask import render_template, url_for, flash, redirect

from flaskr import app, db, bcrypt
from flaskr.models import User, Post
from flaskr.forms import RegistrationForm, LoginForm


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

# ROUTES ################################################################################################################################

# HOME
@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html", posts=posts)

# ABOUT
@app.route("/about")
def about(): 
    return render_template("about.html", title="About")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit(): 
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data, 
            email = form.email.data, 
            password = hashed_pw
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# LOGIN
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