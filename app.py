from flask import Flask, request, render_template, redirect
import random
import sqlite3

# Start Flask App
app = Flask(__name__)

# Index Route
@app.route("/")
def index():
    return render_template("index.html")

# What to Eat Version 2 - W/ SQL
@app.route("/addafood", methods=["POST", "GET"])
def add_a_food():
    

    if request.method == "GET":
        return render_template("addafood.html")

    elif request.method == "POST":
        # Create Connection to Database
        db = sqlite3.connect("food.db")
        db.text_factory = str
        cursor =   db.cursor()

        new_place = request.form.get("restaurant")
        new_recipe = request.form.get("recipe")

        if new_place:
            cursor.execute("INSERT INTO restaurants (name) VALUES (?)", [new_place])

        if new_recipe:
            cursor.execute("INSERT INTO meals (name) VALUES (?)", [new_recipe])

        db.commit()
        cursor.close()

        return redirect("/options")

    
@app.route("/options")
def list_options():

    # Create Connection to Database
    db = sqlite3.connect("food.db")
    db.text_factory = str
    cursor =   db.cursor()

    recipe_rows = cursor.execute("SELECT * FROM meals").fetchall()
    restaurant_rows = cursor.execute("SELECT * FROM restaurants").fetchall()

    return render_template("foodoptions.html", recipes = recipe_rows, restaurants = restaurant_rows)
    cursor.close()

@app.route("/selectedfood", methods=["POST"])
def select_food():
    eating_options = request.form.getlist("food_choice")
    result = random.choice(eating_options)
    return render_template("selectedfood.html", result=result)