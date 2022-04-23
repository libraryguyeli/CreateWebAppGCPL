from flask import Flask, request, render_template, redirect
import random
import sqlite3



# Start Flask App
app = Flask(__name__)

# Index Route
@app.route("/")
def index():
    return render_template("index.html")

#Random Number Generator
@app.route("/<int:number>")
def random_number(number):
    randomized = random.randint(0, number)
    result = "{:,}".format(randomized)
    return render_template("randomnumber.html", result=result)

# COIN TOSS
@app.route("/cointoss")
def coin_toss():
    coin = random.randint(0,1)
    print(coin)
    return render_template("cointoss.html", result=coin)

# SCRAMBLE A WORD
@app.route("/getword")
def get_word():
    return render_template("getword.html")

@app.route("/scrambleword", methods = ["POST"])
def scramble_word():
    word = request.form.get("word")
    charlist = list(word)
    random.shuffle(charlist)
    join_scramble = "".join(charlist).lower()
    return render_template("scrambleword.html", result = join_scramble)

# WHERE TO EAT RANDOMIZER
@app.route("/selections")
def choices():
    return render_template("restaurantoptions.html")


@app.route("/selectedplace", methods=["POST"])
def select_place():
    places = request.form.getlist("restaurants")
    print(places)
    result = random.choice(places)
    print("Choice:", result)
    return render_template("selectedplace.html", result=result)

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
    print(result)
    return render_template("selectedfood.html", result=result)