from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Hello World")

app = Flask(__name__)
@app.route('//')
def elcome():
    return("Welcome!")