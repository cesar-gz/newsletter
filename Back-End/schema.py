from pydantic import BaseModel
from typing import List, Optional

# first table is a list of email addresses mapped to user id
class User(BaseModel):
    userId: Optional[int]
    name: str
    email: str
    topics: List[int]

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
    id: Optional[int]
    userId: int
    newsletter : str
