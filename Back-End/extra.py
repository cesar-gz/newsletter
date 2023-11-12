""" to go in populate if I want more mock data to test/query the database with"""

from schema import User, News, Wants, Staging

users = [
    User(userId=1, name="James", email="james@example.com", topics=[1,9]),
    User(userId=2, name="Mary", email="mary@example.com", topics=[2,5]),
    User(userId=3, name="Robert", email="robert@example.com", topics=[4,6]),
    User(userId=4, name="Linda", email="linda@example.com", topics=[10,12]),
    User(userId=5, name="Michael", email="michael@example.com", topics=[3,7]),
    User(userId=6, name="Elizabeth", email="elizabeth@example.com", topics=[6,8]),
    User(userId=7, name="David", email="david@example.com", topics=[8,9]),
    User(userId=8, name="Jennifer", email="jennifer@example.com", topics=[1,2]),
    User(userId=9, name="Richard", email="richard@example.com", topics=[1,9,11]),
    User(userId=10, name="Michelle", email="michelle@example.com", topics=[2,5,12]),
    User(userId=11, name="Brian", email="brian@example.com", topics=[2,3]),
    User(userId=12, name="Kimberly", email="kimberly@example.com", topics=[4,6]),
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


print("Tables created successfully.")
print("Begin populating data into tables...")

# start inserting data into tables
cursor = conn.cursor()
for u in users:
    cursor.execute(
        """
        INSERT INTO user (userId, name, email)
        VALUES (?, ?, ?)
        """,
        (u.userId, u.name, u.email),
    )

for n in newsTopics:
    cursor.execute(
        """
        INSERT INTO news (id, topic)
        VALUES (?, ?)
        """,
        (n.id, n.topic)
    )

print("Database finished populating.")

conn.commit()
cursor.close()
conn.close()
