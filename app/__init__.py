#This file intializes a Python module. Without it, Python will not recognize the app directory as a module.

from flask import Flask
from flask_pymongo import PyMongo

#Initialize the app

app = Flask(__name__, instance_relative_config=True)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://pretty:printed@ds135594.mlab.com:35594/connect_to_mongo'

mongo = PyMongo(app)

#Load the views
from app import views

#Load the config file
app.config.from_object('config')
