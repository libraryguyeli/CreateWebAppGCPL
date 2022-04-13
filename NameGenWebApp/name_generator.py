'''Creating the database for the random dwarf, elf, fairy, and minotaur names.'''

import sqlite3
import csv
import random

db = sqlite3.connect("namegen.db")
cur = db.cursor()

# DB FUNCTIONS #
def dwarf_table():
    db.execute("CREATE TABLE IF NOT EXISTS dwarf (id INTEGER PRIMARY KEY, first STRING, last STRING, gender STRING);")

    with open("CSVs/dwarfnames.csv", "r") as file:
        csv_file = csv.DictReader(file)
        # next(csv_file) # This makes it skip the first entry.

        for row in csv_file:
            id = row["ID"]
            first = row["First"]
            last = row["Last"]
            gender = row["Gender"]

            cur.execute("INSERT or IGNORE INTO dwarf (id, first, last, gender) VALUES (?,?,?,?)", (id, first, last, gender))
    db.commit()

def elf_table():
    db.execute("CREATE TABLE IF NOT EXISTS elf (id INTEGER PRIMARY KEY, first STRING, last STRING, gender STRING);")

    with open("CSVs/elfnames.csv", "r") as file:
        csv_file = csv.DictReader(file)

        for row in csv_file:
            id = row["ID"]
            first = row["First"]
            last = row["Last"]
            gender = row["Gender"]

            cur.execute("INSERT or IGNORE INTO elf (id, first, last, gender) VALUES (?,?,?,?)", (id, first, last, gender))
    db.commit()

def fairy_table():
    db.execute("CREATE TABLE IF NOT EXISTS fairy (id INTEGER PRIMARY KEY, first STRING, last STRING, gender STRING);")

    with open("CSVs/fairynames.csv", "r") as file:
        csv_file = csv.DictReader(file)

        for row in csv_file:
            id = row["ID"]
            first = row["First"]
            last = row["Last"]
            gender = row["Gender"]

            cur.execute("INSERT or IGNORE INTO fairy (id, first, last, gender) VALUES (?,?,?,?)", (id, first, last, gender))
    db.commit()

def minotaur_table():
    db.execute("CREATE TABLE IF NOT EXISTS minotaur (id INTEGER PRIMARY KEY, first STRING, gender STRING);")

    with open("CSVs/minotaurnames.csv", "r") as file:
        csv_file = csv.DictReader(file)

        for row in csv_file:
            id = row["ID"]
            first = row["First"]
            gender = row["Gender"]

            cur.execute("INSERT or IGNORE INTO minotaur (id, first, gender) VALUES (?,?,?)", (id, first, gender))
    db.commit()

# DWARVES #
# dwarf_table()

# dwarf_first = db.execute("SELECT first FROM dwarf;")
# dwarf_last = db.execute("SELECT last FROM dwarf;")

# for name in dwarf_first:
#     print(name[0])
# print("\n")
# for name in dwarf_last:
#     print(name[0])

# # ELVES #
# elf_table()

# elf_first = db.execute("SELECT first FROM elf ORDER BY random() LIMIT 1;")
# elf_last = db.execute("SELECT last FROM elf ORDER BY random() LIMIT 1;")

# for name in elf_first:
#     name1 = name[0]
# print("\n")
# for name in elf_last:
#     name2 = name[0]

# print("{} {}".format(name1, name2))

# # FAIRIES #
# fairy_table()

# fairy_first = db.execute("SELECT first FROM fairy;")
# fairy_last = db.execute("SELECT last FROM fairy;")

# for name in fairy_first:
#     print(name[0])
# print("\n")
# for name in fairy_last:
#     print(name[0])

# MINOTAURS #
# minotaur_table()
# minotaur_first = db.execute("SELECT first FROM minotaur;")

# for name in minotaur_first:
#     print(name[0])