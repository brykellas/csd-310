# Bryce Kellas
# Module 8 - Movies: Updates & Deletes
# GitHub: https://github.com/brykellas/csd-310.git
#
# Use cursor to run SELECT, UPDATE, INSERT and DELETE queries on the film table in the movies database

import mysql.connector
from mysql.connector import errorcode

def show_films(cursor, title):
    """ Execute inner join on all tables and iterate over the data to display to user """
    
    # join query 
    cursor.execute("""
        SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' 
        FROM film 
        INNER JOIN genre ON film.genre_id=genre.genre_id 
        INNER JOIN studio ON film.studio_id=studio.studio_id
    """)

    # Get results from cursor
    films = cursor.fetchall()

    # Displays label for data section
    print("\n -- {} --".format(title))

    # iterate over film data and display the data
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1],film[2], film[3]))

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

# Displaying original film table
show_films(cursor, "DISPLAYING FILMS")


# Inserting a record into the film table 
cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('The Bourne Ultimatum', 2007, 115, 'Paul Greengrass', 3, 3)
""")

# Displaying film table after the insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


# Update a record in film table 
cursor.execute("""
    UPDATE film 
    SET genre_id = 1
    WHERE film_id = 2
""")

# Displaying film table after the update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")


# Delete a record in film table 
cursor.execute("""
    DELETE FROM film 
    WHERE film_name = 'Gladiator'
""")

# Displaying film table after the update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

db.close()