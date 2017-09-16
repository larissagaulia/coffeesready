#This file intializes a Python module. Without it, Python will not recognize the app directory as a module.

from flask import Flask
from flask_pymongo import PyMongo

#Initialize the app

app = Flask(__name__, instance_relative_config=True)
mongo = PyMongo(app)

#Load the views
from app import views

#Load the config file
app.config.from_object('config')
