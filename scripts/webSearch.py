"""
make sure to first run the command `pip install -U g4f`
"""

import g4f
from g4f.Provider import ( Bing )
import sys

if len(sys.argv) != 3:
    print('Must include 2 command line arguments, Example: python webSearch.py "<topic>" <output.txt>')
    sys.exit(1)

topic = sys.argv[1]
filePath = "output/" + sys.argv[2]

print("starting web search script... takes 30 seconds...")

# get the response
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.Bing,
    messages=[{"role": "user", "content": topic}],
    stream=True,
)

answer = ""
for message in response:
    answer += message

with open(filePath, "w", encoding="utf-8") as file:
    file.write(answer)

print("Script finished. A new file was created.")
