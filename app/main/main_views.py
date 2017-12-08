from flask import Flask
from . import main as main



@main.route('/')
def hello_world():
    return 'Hello World!'


