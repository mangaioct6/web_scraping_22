#!/usr/bin/env python
from rest_function import my_function # importing function py file
from flask import Flask, render_template
import pandas as pd

# creating an object for flask app
app = Flask(__name__)

# route decorator helps us to create an endpoints for our API
@app.route("/")
def hi():
    return "Scraping Nearby Restaurants data!" 

@app.route("/scrape")
def scrape():
    pass

# this route will print all our restaurant data
@app.route("/all")
def nearby():
    return my_function()
    
if __name__ == "__main__":
    app.run(debug=True)