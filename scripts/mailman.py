import subprocess
import requests

apiUrl = "http://localhost:5000"

# calculate how many times to run for loop
DB_Response = requests.get(f"{apiUrl}/users/ids")
response_json = DB_Response.json()
users = response_json.get("Users")
numOfUsers = len(users)

for i in range(1, numOfUsers+1):
  # get the users name and email
  DB_Response = requests.get(f"{apiUrl}/users/{i}")
  response_json = DB_Response.json()
  user = response_json.get("user")
  topics = response_json.get("topics", [])

  # arg1 to pass is subject, arg2 is recipient
  subject = "Dear " + str(user["name"]) + " this is your personal newsletter"
  recipient = user["email"]

  # arg3 is body to send in email
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
  print("Mail has been sent to user " + str(i) + "!")
