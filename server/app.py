#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)  # instance of flash app

@app.route('/')  # registering the index function with the app
def index():
    return "<h1>Weldcome to my App!</h1>"

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}'

if __name__ == '__main__':     # this script enables us to say run the app as a script by just saying "python app.py"
    app.run(port=555, debug=True) # debut=True enables the server to restart whenever we change app.py