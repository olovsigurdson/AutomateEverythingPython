import datetime

import yagmail
import os
import time
from datetime import datetime as dt
sender = "olov.sigurdson@gmail.com"
receiver = "olov.sigurdson@tietoevry.com"

subject = "This is the subject"
content = """
Här kommer lite innehåll! Hej!
"""
#os.getenv("PASSWORD")
#App password os.getenv("PASSWORD")

print(dt.now().strftime("%H%M"))

run = True
while run:
    current_time = dt.now().strftime("%H%M")
    if current_time == '1247':
        yag = yagmail.SMTP(user=sender, password="cuayewzipxmbnvfq")
        yag.send(to=receiver, subject=subject, contents=content)
        print("Email sent!")
    time.sleep(60)


