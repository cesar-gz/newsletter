import re

header = "These links below are sources you can read for more information.\n\n"
patterns_to_remove = [r'\[\^1\^\]', r'\[\^2\^\]', r'\[\^3\^\]', r'\[\^4\^\]', r'\[\^5\^\]', r'\[\^6\^\]', r'\[\^7\^\]', r'\[\^8\^\]', r'\[\^9\^\]', r'\"\"']

for i in range(1,13):
  filePath = "output/newsTopic" + str(i) + ".txt"
  fileContent = ""

  with open(filePath, "r", encoding="utf-8") as file:
      fileContent = file.read()

  for pattern in patterns_to_remove:
      fileContent = re.sub(pattern, '', fileContent)

  body = header + fileContent

  body = body.replace("- ", "\n")

  with open(filePath, 'w', encoding="utf-8") as file:
      file.write(body)

print("Formatter finished.")
