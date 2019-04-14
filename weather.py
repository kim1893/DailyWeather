import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import smtplib

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

apiKey = os.getenv('WEATHERAPIKEY')

url = 'https://api.openweathermap.org/data/2.5/weather?zip=47906,us&APPID=' + apiKey

r = requests.get(url)
data = r.json()
tempInF = round(int(data['main']['temp']) * (9/5) - 459.67, 2)
desc = ""
for weather in data['weather']:
    desc += weather['description'] + ", "
desc = desc[:-2]

msg = "Degrees in Farenheit: " + str(tempInF) + "\nDescription: " + desc
sent_from = "hurricanesnerd@gmail.com"
to = "junsookim23@gmail.com"
subject = "Daily Weather for Jun Soo!"
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, msg)

#print(msg)
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hurricanesnerd@gmail.com", str(os.getenv('GMAILPASS')))
    server.sendmail("hurricanesnerd@gmail.com", "junsookim23@gmail.com", email_text)
    print("Email sent!")
except:
    print("Something went wrong")
server.close()


