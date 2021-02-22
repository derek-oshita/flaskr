import os

from flask import Flask 

app = Flask(__name__)


@app.route("/")
def hello_world(): 
    return "<h1>Home page!</h1>"

@app.route("/about")
def about(): 
    return "About page..."

if __name__ == "__main__": 
    app.run(debug=True, port=3000)