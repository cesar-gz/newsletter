import sqlite3
import os
from schema import User, News, Wants, Staging

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
                        userId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name text NOT NULL,
                        email text NOT NULL
                 ); """
    createTable(conn, usersTable)

    newsTable = """ CREATE TABLE IF NOT EXISTS news (
                        id integer NOT NULL PRIMARY KEY UNIQUE,
                        topic text NOT NULL
                 ); """
    createTable(conn, newsTable)

    wantsTable = """ CREATE TABLE IF NOT EXISTS wants (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userId integer,
                        wantedNews integer,
                        FOREIGN KEY(userId) REFERENCES user(userId)
                 ); """
    createTable(conn, wantsTable)

    stagingTable = """ CREATE TABLE IF NOT EXISTS staging (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userId integer,
                        newsletter text NOT NULL,
                        FOREIGN KEY(userId) REFERENCES user(userId)
                 ); """
    createTable(conn, stagingTable)
    
    print("Database connection closed successfully.")

if __name__ == "__main__":
    populateDatabase()
