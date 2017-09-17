#This file contains all the routes for our application.
#This will tell Flask what to display on which path.
from datetime import datetime
from flask import render_template
from flask import request

from app import app
from app import mongo

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/add')
def add():
  coffee_status = mongo.db.coffee_status
  now = str(datetime.now())
  coffee_status.insert({'status': 'done', 'timestamp': now})
  return 'Coffee status added'

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404
