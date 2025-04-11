from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1> Welcome to Flask Min App! {ime} </h1>'


@app.route('/name')
def name():
    return '<h1> Welcome to Flask Min App! NAME page </h1>'
