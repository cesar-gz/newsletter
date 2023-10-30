import contextlib
import sqlite3

from fastapi import Depends, HTTPException, APIRouter, status
from schema import User

router = APIRouter()
database = "database.db"

# Connect to the database
def getDb():
    with contextlib.closing(sqlite3.connect(database, check_same_thread=False)) as db:
        db.row_factory = sqlite3.Row
        yield db

# ========================================== users ==========================================

# retrieve all user ids
@router.get("/users/ids", tags=['User'])
def get_all_user_ids(db:sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    # fetch user data from db
    cursor.execute(
        """
        SELECT user.userId
        FROM user
        """
    )

    userData = cursor.fetchall()
    # check if users exist
    if not userData:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return {"Users" : userData}


# get a users email
@router.get("/users/{userId}/email", tags=['User'])
def get_users_email(userId: int, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    # fetch user data from db
    cursor.execute(
        """
        SELECT * FROM user
        WHERE userId = ?
        """, (userId,)
    )

    # check if user exists
    userData = cursor.fetchone()
    if not userData:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    return {"User": userData}


# add a user to the database
@router.post("/users/subscribe/{userId}", tags=['User'])
def add_user(userId: int, name: str, email: str, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    # check if user already exists
    cursor.execute("SELECT * FROM user WHERE userId = ?", (userId,))
    userData = cursor.fetchone()

    if userData:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists. Use a new userId.")

    cursor.execute(
        """
        INSERT INTO user (userId, name, email)
        VALUES (?, ?, ?)
        """, (userId, name, email)
    )

    db.commit()

    # fetch new data
    cursor.execute("SELECT * FROM user WHERE userId = ?", (userId,))
    newUser = cursor.fetchone()
    return newUser


# ========================================== news ==========================================

# get all news topic ids
@router.get("/news/topics", tags=['News'])
def get_topics(db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    # fetch news data from db
    cursor.execute(
        """
        SELECT * FROM news
        """
    )

    # check if news exists
    newsData = cursor.fetchall()
    if not newsData:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No news topics found.")

    return {"Topics": newsData}

# ========================================== wants ==========================================


# ========================================== staging ==========================================
