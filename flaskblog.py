import os

from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET KEY'] = 

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

if __name__ == "__main__": 
    app.run(debug=True, port=3000)