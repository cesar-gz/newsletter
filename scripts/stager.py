""" pip install requests """

import subprocess
import requests

scriptPath = 'webSearch.py'
filePath = "prompts.txt"
fileContent = ""

with open(filePath, "r", encoding="utf-8") as file:
    fileContent = file.read()

fileContent = fileContent.split('*')
fileContent.pop()

# conduct web searches
for i in range(2):
    arg1 = fileContent[i]
    arg2 = 'newsTopic' + str(i+1) + '.txt'
    command = ['python', scriptPath, arg1, arg2]
    subprocess.run(command)

# start adding new files to database
apiUrl = "http://localhost:5000"

for i in range(2):
  print("sending request " + str(i+1) + "...")

  filePath = "output/newsTopic" + str(i+1) + ".txt"
  fileContent = ""

  with open(filePath, "r", encoding="utf-8") as file:
    fileContent = file.read()

  data = {
      "id" : i,
      "userId": i,
      "newsletter": fileContent
  }

  DB_Response = requests.post(f"{apiUrl}/staging/create", json=data)
  print(f"Status Code: {DB_Response.status_code}")
  print("Response Content:")
  print(DB_Response.json())
