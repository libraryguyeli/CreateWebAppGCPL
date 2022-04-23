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
        # Dwarf table
        if species == "dwarf":
            if gender == "female":
                first = cursor.execute("SELECT first FROM dwarf WHERE gender = 'F' ORDER BY random() LIMIT 1;")
            else:
                first = cursor.execute("SELECT first FROM dwarf WHERE gender = 'M' ORDER BY random() LIMIT 1;")
            first = cursor.fetchall()
            last = cursor.execute("SELECT last FROM dwarf ORDER BY random() LIMIT 1;")
            last = cursor.fetchall()
            first_names.append(first)
            last_names.append(last)

        # Elf table
        if species == "elf":
            if gender == "female":
                first = cursor.execute("SELECT first FROM elf WHERE gender = 'F' ORDER BY random() LIMIT 1;")
            elif gender == "male":
                first = cursor.execute("SELECT first FROM elf WHERE gender = 'M' ORDER BY random() LIMIT 1;")
            else:
                first = cursor.execute("SELECT first FROM elf WHERE gender = 'N' ORDER BY random() LIMIT 1;")
            first = cursor.fetchall()
            last = cursor.execute("SELECT last FROM elf ORDER BY random() LIMIT 1;")
            last = cursor.fetchall()
            first_names.append(first)
            last_names.append(last)

        # Fairy table
        if species == "fairy":
            if gender == "female":
                first = cursor.execute("SELECT first FROM fairy WHERE gender = 'F' ORDER BY random() LIMIT 1;")
            else:
                first = cursor.execute("SELECT first FROM fairy WHERE gender = 'M' ORDER BY random() LIMIT 1;")     
            first = cursor.fetchall()
            last = cursor.execute("SELECT last FROM fairy ORDER BY random() LIMIT 1;")
            last = cursor.fetchall()
            first_names.append(first)
            last_names.append(last)

        # Minotaur table
        if species == "minotaur":
            if gender == "female":
                first = cursor.execute("SELECT first FROM minotaur WHERE gender = 'F' ORDER BY random() LIMIT 1;")
            elif gender == "male":
                first = cursor.execute("SELECT first FROM minotaur WHERE gender = 'M' ORDER BY random() LIMIT 1;")
            else:
                first = cursor.execute("SELECT first FROM minotaur WHERE gender = 'N' ORDER BY random() LIMIT 1;")
            first = cursor.fetchall()
            last = ''
            first_names.append(first)
            last_names.append(last)
    
    # Close the cursor
    cursor.close()
    
    # Return the template with capitalized species, user-entered number for iterating through the list of names, first and last name lists
    return render_template("result.html", species=species.title(), number=number, first_names=first_names, last_names=last_names)