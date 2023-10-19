import contextlib
import sqlite3

from fastapi import Depends, HTTPException, APIRouter, status
from schemas import Class

router = APIRouter()
database = "database.db"

# Connect to the database
def get_db():
    with contextlib.closing(sqlite3.connect(database, check_same_thread=False)) as db:
        db.row_factory = sqlite3.Row
        yield db