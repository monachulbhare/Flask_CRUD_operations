import smtplib
from email.mime.text import MIMEText

senders = "vaishnavichulbhare7447@gmail.com"
receiver= "poojabhagwat9257@gmail.com"
print({"Sender":senders,"Receiver":receiver})


import sys
sys.exit()
from flask import Flask

app = Flask(__name__)
@app.route('/')
def add():
    return "addition performed"
if __name__ == "__main__":
    app.run()