from pydantic import BaseModel
from typing import List

# first table is a list of email addresses mapped to user id
class User(BaseModel):
    userId: int
    name: str
    email: str

# second table to hold different news topics
class News(BaseModel):
    id: int
    topic: str

# third table is list of each user id attached to that users news topics
class Wants(BaseModel):
    id: int
    userId: int
    topics: List[News] = []

# fourth table is list of completed formatted emails to be sent out
class Staging(BaseModel):
    id: int
    userId: int
    newsletter : str