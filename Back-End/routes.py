import contextlib
import sqlite3

from fastapi import Depends, HTTPException, APIRouter, status
from schema import User, Staging

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


# get a users information
@router.get("/users/{userId}", tags=['User'])
def get_a_users_info(userId: int, db: sqlite3.Connection = Depends(getDb)):
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

    # Fetch the user's topics
    cursor.execute("SELECT wantedNews FROM wants WHERE userId = ?", (userId,))
    userTopics = [row[0] for row in cursor.fetchall()]

    return {"user": userData, "topics": userTopics}

# add a user to the database
@router.post("/users/subscribe/", tags=['User'])
def create_a_user(userInfo : User, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    userInfo.userId = None

    cursor.execute(
        """
        INSERT INTO user (name, email)
        VALUES (?, ?)
        """, (userInfo.name, userInfo.email)
    )

    db.commit()

    # Fetch the user with the auto-incremented user ID
    lastUserId = cursor.lastrowid

    # Insert the user's topic interests into the "Wants" table
    for topic in userInfo.topics:
        cursor.execute(
            """
            INSERT INTO wants (userId, wantedNews)
            VALUES (?, ?)
            """, (lastUserId, topic)
        )

    db.commit()

    return {"message": "User successfully created."}

@router.delete("/users/unsubscribe/{userId}", tags=['User'])
def delete_a_user(userId: int, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    # Check if the user exists
    cursor.execute("SELECT * FROM user WHERE userId = ?", (userId,))
    user_data = cursor.fetchone()

    if user_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Delete the user from the database
    cursor.execute("DELETE FROM user WHERE userId = ?", (userId,))
    db.commit()

    return {"message": "User deleted successfully"}


# ========================================== news ==========================================

# get all news topic ids
@router.get("/news/topics", tags=['News'])
def get_all_news_topics(db: sqlite3.Connection = Depends(getDb)):
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


# ========================================== staging ==========================================
# A way for me to see what is about to be sent out
@router.get("/staging/{userId}", tags=["Staging"])
def get_staging_data_for_a_user(userId: int, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM staging WHERE userId = ?", (userId,))
    staging_data = cursor.fetchone()

    if staging_data is None:
        raise HTTPException(status_code=404, detail="There is nothing prepared for the specified User Id")

    return staging_data

# A way for the AI to add the email body to the database
@router.post("/staging/create", tags=["Staging"])
def store_created_email(stagingData: Staging, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    stagingData.id = None

    cursor.execute(
        """
        INSERT INTO staging (userId, newsletter)
        VALUES (?, ?)
        """, (stagingData.userId, stagingData.newsletter)
    )

    db.commit()

    cursor.execute("SELECT * FROM staging WHERE userId = ?", (stagingData.userId,))

    return {"message": "The email was stored successfully."}

# delete a stored email
@router.delete("/staging/delete/{userId}", tags=["Staging"])
def delete_stored_email(userId: int, db: sqlite3.Connection = Depends(getDb)):
    cursor = db.cursor()

    # Check if a staging row with the specified userId exists
    cursor.execute("SELECT * FROM staging WHERE userId = ?", (userId,))
    staging_data = cursor.fetchone()

    if staging_data is None:
        raise HTTPException(status_code=404, detail="There is no stored email for the specified User Id.")

    # Delete the staging row with the provided userId
    cursor.execute("DELETE FROM staging WHERE userId = ?", (userId,))
    db.commit()

    return {"message": "The stored email was deleted successfully."}
