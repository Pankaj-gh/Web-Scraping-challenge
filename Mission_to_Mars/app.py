from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape_mars

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

collections = mongo.db.mars_collection
collections.drop()

@app.route('/')
def home():
    results=list(listings.find())
    return render_template('index.html',listing_results=results)

@app.route("/scrape")
def scraper():

    scraped_data=scrape_mars.scrape()