import sqlite3
import os
from schemas import User, News, Wants, Staging

""" create sample data to test/query the database with """

users = [
    User(userId=1, name="James", email="james@example.com"),
    User(userId=2, name="Mary", email="mary@example.com"),
    User(userId=3, name="Robert", email="robert@example.com"),
    User(userId=4, name="Linda", email="linda@example.com"),
    User(userId=5, name="Michael", email="michael@example.com"),
    User(userId=6, name="Elizabeth", email="elizabeth@example.com"),
    User(userId=7, name="David", email="david@example.com"),
    User(userId=8, name="Jennifer", email="jennifer@example.com"),
    User(userId=9, name="Richard", email="richard@example.com"),
    User(userId=10, name="Michelle", email="michelle@example.com"),
    User(userId=11, name="Brian", email="brian@example.com"),
    User(userId=12, name="Kimberly", email="kimberly@example.com"),
]

newsTopics = [
    News(id=1, topic="World News"),
    News(id=2, topic="U.S. News"),
    News(id=3, topic="Republican Politics"),
    News(id=4, topic="Democratic Politics"),
    News(id=5, topic="Business"),
    News(id=6, topic="Science"),
    News(id=7, topic="Health"),
    News(id=8, topic="Religion"),
    News(id=9, topic="Sports"),
    News(id=10, topic="Gaming"),
    News(id=11, topic="Finance"),
    News(id=12, topic="Technology"),
]

userWants = [
    Wants(id=1,
          userId=1, 
          topics=[
              News(id=1, topic="World News"),
              News(id=9, topic="Sports"), 
            ]
          ),
    Wants(id=2,
          userId=4, 
          topics=[
              News(id=2, topic="U.S. News"),
              News(id=5, topic="Business"), 
            ]
          ),
    Wants(id=3,
          userId=7, 
          topics=[
              News(id=4, topic="Democratic Politics"),
              News(id=6, topic="Science"), 
            ]
          ),
    Wants(id=4,
          userId=11, 
          topics=[
              News(id=10, topic="Gaming"),
              News(id=12, topic="Technology"), 
            ]
          )
]

readyToShip = [
    Staging(id=1, userId=1, newsletter="The world is dying."),
    Staging(id=2, userId=4, newsletter="The world is thriving."),
    Staging(id=3, userId=7, newsletter="The stock market crashed."),
    Staging(id=4, userId=11, newsletter="The economy is booming."),
]

""" set up the database and define SQL calls """

# remove database if it exists before creating and populating it
if os.path.exists("database.db"):
    os.remove("database.db")

# create database connection to the SQLite database
def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        return conn
    except sqlite3.Error as e:
        print("Error: ", e)
    return conn

# create a table with given SQL CREATE statement
def createTable(conn, createTableSQL):
    try:
        c = conn.cursor()
        c.execute(createTableSQL)
    except sqlite3.Error as e:
        print("Error: ", e)

# select SQL statement
def selectQuery(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print("Error: ", e)

""" begin populating the database """
def populateDatabase():

    print("Connecting to Database...")
    database = "database.db"
    conn = createConnection(database)
    print("Database successfully connected.")

    print("Creating Tables...")

    usersTable = """ CREATE TABLE IF NOT EXISTS user (
                        userId integer NOT NULL PRIMARY KEY UNIQUE,
                        name text NOT NULL
                        email text NOT NULL
                 ); """
    createTable(conn, usersTable)

    newsTable = """ CREATE TABLE IF NOT EXISTS news (
                        id integer NOT NULL PRIMARY KEY UNIQUE,
                        topic text NOT NULL
                 ); """
    createTable(conn, newsTable)

    wantsTable = """ CREATE TABLE IF NOT EXISTS wants (
                        id integer NOT NULL PRIMARY KEY UNIQUE,
                        wantedNews integer,
                        FOREIGN KEY(userId) REFERENCES user(userId)
                 ); """
    createTable(conn, wantsTable)

    stagingTable = """ CREATE TABLE IF NOT EXISTS staging (
                        id integer NOT NULL PRIMARY KEY UNIQUE,
                        newsletter text NOT NULL
                        FOREIGN KEY(userId) REFERENCES user(userId)
                 ); """
    createTable(conn, stagingTable)

    print("Tables created successfully.")
    print("Beginn populating data into tables...")
    
    # start inserting data into tables
    cursor = conn.cursor()
    for u in users:
        cursor.execute(
            """
            INSERT INTO user (userId, name, email)
            VALUES (?, ?, ?)
            """,
            (users.userId, users.name, users.email)
        )

    for n in newsTopics:
        cursor.execute(
            """
            INSERT INTO news (id, topic)
            VALUES (?, ?)
            """,
            (newsTopics.id, newsTopics.topic)
        )
    
    for w in userWants:
        cursor.execute(
            """
            INSERT INTO wants (id, userId, wantedNews)
            VALUES (?, ?, ?)
            """,
            (userWants.id, userWants.userId, userWants.topics)
        )

    for r in readyToShip:
        cursor.execute(
            """
            INSERT INTO staging (id, userId, newsletter)
            VALUES (?, ?, ?)
            """,
            (readyToShip.id, readyToShip.userId, readyToShip.newsletter)
        )
    
    print("Database finished populating.")

    conn.commit()
    cursor.close()
    conn.close()

    print("Database connection closed successfully.")

if __name__ == "__main__":
    populateDatabase()