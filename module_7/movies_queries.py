# Bryce Kellas
# Module 7 - Movies: Movies Table Queries
# GitHub: https://github.com/brykellas/csd-310.git
# mysql-connector-python test

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["host"],config["host"],config["database"]))

    input("\n\n Press enter to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()

cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()

cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
films = cursor.fetchall()

cursor.execute("SELECT * FROM film ORDER BY film_director")
films_by_director = cursor.fetchall()


print("\n-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

print("-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

print("-- DISPLAYING Short Films RECORDS --")
for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[1], film[3]))

print("-- DISPLAYING Director RECORDS in Order --")
for film in films_by_director:
    print("Film Name: {}\nDirector: {}\n".format(film[1], film[4]))

db.close()
