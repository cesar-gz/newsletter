import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import sys

if len(sys.argv) != 4:
    print('Must include 3 command line arguments, Example: python sendEmails.py "<subject>" "<recipients email>" "<body>"')
    sys.exit(1)

load_dotenv()

sender_email = os.getenv("EMAIL")
pwd = os.getenv("PWD")
recipient_email = sys.argv[2]

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = sys.argv[1]

# Add the email body
body = sys.argv[3]

message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Start the TLS connection
    server.starttls()
    server.login(sender_email, pwd)
    server.sendmail(sender_email, recipient_email, message.as_string())
