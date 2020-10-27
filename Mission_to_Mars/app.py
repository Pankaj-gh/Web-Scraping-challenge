from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape_mars

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

collections = mongo.db.mars_collection
collections.drop()

@app.route('/')
def index():
    listing_results=collections.find()
    return render_template('index.html',listing_results=listing_results)

@app.route("/scrape")
def scraper():

    scraped_data=scrape_mars.scrape()
    collections.insert_many(scraped_data)


    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)