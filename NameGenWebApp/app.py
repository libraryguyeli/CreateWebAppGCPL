'''This app pulls fantasy names randomly from a database based on user-entered responses:
    species, gender, number of names.'''

# Importing libraries
from flask import Flask, render_template, request
import sqlite3
import random

# Define the app
app = Flask(__name__)

# Index page: GET form from HTML file, POST the response
@app.route("/", methods = ["GET", "POST"])
def selections():
    return render_template("index2.html")

# Results page
@app.route("/result", methods = ["GET", "POST"])
def result():
    # Create a connection to the database
    db = sqlite3.connect('namegen.db')
    # For removing unneeded punctuation from results page
    db.row_factory = lambda cursor, row: row[0]
    # Create a cursor object to traverse the database
    cursor = db.cursor()

    # Get and save the responses from the user
    species = request.form.get("species")
    
    # Close the cursor
    cursor.close()
    
    # Return the template with capitalized species, user-entered number for iterating through the list of names, first and last name lists
    return render_template("result2.html", species=species.title())