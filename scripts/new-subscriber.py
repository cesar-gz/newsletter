"""
Ideally, I should have 12 news topic already stored in the database.
This script should then just perform one GET request to get the
new user's request news topics
"""

import subprocess
import requests
import sys

apiUrl = "http://localhost:5000"
name = sys.argv[1]
recipient = sys.argv[2] # the user's email
topics = sys.argv[3]
subject = "Dear " + str(name) + " this is your personal newsletter"
body = ""

# get the news topics the user wants
for topic in topics:
  DB_Response = requests.get(f"{apiUrl}/staging/{topic-1}")
  response_json = DB_Response.json()
  news = response_json.get("newsletter")
  body += str(news) + "\n\n"

# mail man sends email to user
scriptPath = 'sendEmails.py'
command = ['python', scriptPath, subject, recipient, body]
subprocess.run(command)
print("Mail has been sent to user " + str(name))
