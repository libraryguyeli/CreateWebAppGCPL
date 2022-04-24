'''This app pulls fantasy names randomly from a database based on user-entered responses:
    species and number of names.'''

# Importing libraries
from flask import Flask, render_template, request
import sqlite3
import random

# Define the app
app = Flask(__name__)

# Index page: GET form from HTML file, POST the response
@app.route("/", methods = ["GET", "POST"])
def selections():
    return render_template("index.html")

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
    gender = request.form.get("gender")
    number = int(request.form.get("number")) # Convert this to an integer in order to use it mathematically
    
    # Create two lists to hold first and last names based on number in user response
    first_names = []
    last_names = []

    # Iterate based on user-entered number to return however many names
    for i in range(number):
        
        # Get first name
        first = cursor.execute("SELECT first FROM " + species + " ORDER BY random() LIMIT 1;")
        first = cursor.fetchall()
        first_names.append(first)

        # Get last name, unless it is a minotaur
        if species != "minotaur":
            last = cursor.execute("SELECT last FROM " + species + " ORDER BY random() LIMIT 1;")
            last = cursor.fetchall()
        else:
            last = ''
        last_names.append(last)
    
    # Close the cursor
    cursor.close()
    
    # Return the template with capitalized species, user-entered number for iterating through the list of names, first and last name lists
    return render_template("result.html", species=species.title(), first_names=first_names, last_names=last_names, number=number)