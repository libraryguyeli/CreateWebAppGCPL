# IMPORT LIBRARIES
import csv
import sqlite3

# Create Connection to Database
db = sqlite3.connect("imdb.db")
db.text_factory = str
db.row_factory = lambda cursor, row: row[0]
cur =   db.cursor()

# CONVERT CSV TO SQL DATABASE (using Ranking,IMDByear,IMDBlink,Title,Date,RunTime,Genre,Rating,Score,Votes,Gross)
def convert250():
    print("\nCreating database table: films")
    db.execute("CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, IMDBlink, Ranking INTEGER, IMDByear INTEGER, Title STRING, Date INTEGER, RunTime INTEGER, Genre STRING, Rating REAL, Score REAL, Votes INTEGER, Gross REAL);")

    with open("imdbTop250.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                imdb_link = row["IMDBlink"]
                ranking = row["Ranking"]
                imdb_year = row["IMDByear"]
                title = row["Title"]
                date = row["Date"]
                run_time =  row["RunTime"]
                genres =  row["Genre"]
                rating =  row["Rating"]
                score =  row["Score"]
                votes = row["Votes"]
                gross_revenue =  row["Gross"]
                

                cur.execute("INSERT INTO films (IMDBlink, Ranking, IMDBYear, Title, Date, RunTime, Genre, Rating, Score, Votes, Gross) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (imdb_link, ranking, imdb_year, title, date, run_time, genres, rating, score, votes, gross_revenue))
    print("Table Created Successfully.\n")

    db.commit()

# DELETE DUPLICATES
def del_dups():
    print("Deleting Duplicates.")
    db.execute("CREATE TEMPORARY TABLE tmp_films AS SELECT * FROM films GROUP BY Title")
    db.execute("DELETE FROM films WHERE id NOT IN (SELECT id FROM temp.tmp_films)")
    db.execute("DROP TABLE temp.tmp_films")
    print("Duplicates Deleted.")

convert250()
del_dups()

