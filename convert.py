def open_database():
    # Create Connection to Database
    db = sqlite3.connect("imdb.db")
    db.text_factory = str
    db.row_factory = lambda cursor, row: row[0]
    cur =   db.cursor()

def close_database():
    db.close()

# CONVERT CSV TO SQL DATABASE (using Ranking,IMDByear,IMDBlink,Title,Date,RunTime,Genre,Rating,Score,Votes,Gross)
def convert_to_csv():
    print("\nCreating database table: films")
    db.execute("CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, Poster_Link STRING, Series_Title STRING, Released_Year INTEGER, Certificate STRING, Runtime INTEGER, Genre STRING, IMDB_Rating REAL, Overview STRING, Meta_Score INTEGER, Director STRING, Votes INTEGER, Gross STRING);")

    with open("imdb_top_1000.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                poster_link = row["Poster_Link"]
                series_title = row["Series_Title"]
                released_year = row["Released_Year"]
                certificate = row["Certificate"]
                runtime = row["Runtime"]
                genre = row["Genre"]
                imdb_rating = row["IMDB_Rating"]
                overview = row["Overview"]
                meta_score = row["Meta_score"]
                director = row["Director"]
                votes = row["No_of_Votes"]
                gross = row["Gross"]
                
                cur.execute("INSERT INTO films (Poster_Link, Series_Title, Released_Year, Certificate, Runtime, Genre, IMDB_Rating, Overview, Meta_Score, Director, Votes, Gross) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (poster_link, series_title, released_year, certificate, runtime, genre, imdb_rating, overview, meta_score, director, votes, gross))
    print("Table Created Successfully.\n")

    db.commit()