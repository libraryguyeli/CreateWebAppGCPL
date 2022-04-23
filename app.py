import sqlite3
import csv
from flask import Flask, render_template

# Start Flask App
app = Flask(__name__)


def open_database():
    # Create Connection to Database
    db = sqlite3.connect("imdb.db")
    db.text_factory = str
    db.row_factory = lambda cursor, row: row[0]
    cur =   db.cursor()
    return db, cur

def close_database():
    db.close()


# Index Route
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/result", methods=['GET', 'POST'])
def result():
    # Create Connection to Database
    db = sqlite3.connect("imdb.db")
    # db.text_factory = str
    # db.row_factory = lambda cursor, row: row[0]
    cur =   db.cursor()

    results = db.execute("SELECT * FROM films ORDER BY random() LIMIT 1")

    for result in results:
        title = result[2]
        img_link = result[1].replace('_V1_UX67_CR0,0,67,98_AL_.', '')
        plot = result[8]
        released = result[3]
        runtime = result[5]
        rating = result[7]
        genres = result[6]
        cert = result[4]
        print("Genre", genres)
        print("Certificate: ", cert)
    
    return render_template("result.html", title = title, poster = img_link, plot = plot, released = released, runtime = runtime, rating = rating, genres=genres, certificate=cert)


