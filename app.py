# app.py
from flask import Flask

app = Flask(__file__)

@app.route('/')
def hello():
    return "Hello world!"
