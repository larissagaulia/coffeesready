#This file contains all the routes for our application.
#This will tell Flask what to display on which path.
from flask import render_template
from flask import request

from app import app
from app import mongo

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/done')
def done():
  return addToDatabase('done')

@app.route('/gone')
def gone():
  return addToDatabase('gone')

def addToDatabase(status):
  coffee_status = mongo.db.coffee_status
  coffee_status.insert({'status': status})
  return 'Coffee status added'

@app.route('/get-status')
def getStatus():
  cursor = mongo.db.coffee_status.find().sort([('_id',-1)]).limit(1).next()
  return str(cursor['status'])

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404
