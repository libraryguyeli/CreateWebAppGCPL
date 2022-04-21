from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def selections():
    return render_template("index.html")

@app.route("/result", methods = ["GET", "POST"])
def result():
    db_name = 'namegen.db'
    db = sqlite3.connect(db_name, check_same_thread = False)
    # db.text_factory = str #text_factory is string by default
    db.row_factory = lambda cursor, row: row[0]
    cursor = db.cursor()

    species = request.form.get("species")
    gender = request.form.get("gender")
    number = int(request.form.get("number"))
    
    first_names = []
    last_names = []

    for i in range(number):
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
    
    cursor.close()

    return render_template("result.html", species=species.title(), number=number, first_names=first_names, last_names=last_names)

