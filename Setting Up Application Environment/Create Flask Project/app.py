from flask import flask
from markpsafe import escape
app=Flask(__name__)
@app.route("/")
def index():
    return '<p>Hello, Welcome to Flask!</p>'
@app.route("/<name>")
def hello(name):
    return f'Hello, {escape(name)}!'

@app.route("/users/<username>")
def profile(username):
    return f'Hello '+username
