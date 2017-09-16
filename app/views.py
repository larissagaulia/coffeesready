#This file contains all the routes for our application.
#This will tell Flask what to display on which path.

from flask import render_template
from flask import request

from app import app

@app.route('/')
def index():
  return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404
