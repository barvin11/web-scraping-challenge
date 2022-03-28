from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
# app.config['MONGO_URI']  ="mongodb://localhost:27017/missiontomars"
# mongo = PyMongo(app)
mongo = PyMongo(app, uri="mongodb://localhost:27017/missiontomars")


@app.route("/")
def index():
  print("Hey, this is the main page")
  mars = mongo.db.mars.find_one()

  return render_template("index.html", mars = mars)
  # return "main"
@app.route("/scrape")
def scrape():
  print("hey, this is the scrape page")
  mars = mongo.db.mars
  data = scrape_mars.all_info_func()
  mongo.db.mars.updateOne({}, data, upsert = True)
  return redirect("/", code = 302)
  # return "redirect"
if __name__ == "__main__":
  app.run(debug = True)