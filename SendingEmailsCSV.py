import datetime
from builtins import filter

import yagmail
import os
import time
import csv
from datetime import datetime as dt
sender = "olov.sigurdson@gmail.com"
receiver = "olov.sigurdson@tietoevry.com"


def create_email(name):

    subject_ = f"This is the subject {name}"
    content_ = [f"""
    Här kommer lite innehåll! Hej {name}!
    """,
    "files/2021/December/test1.csv"]
    return [subject_, content_]



yag = yagmail.SMTP(user=sender, password="cuayewzipxmbnvfq")

with open(f"files/contact.csv", "r") as contact_list:
    csv_list = csv.reader(contact_list)

    for row in csv_list:
        namn = row[0]
        email = row[1]
        subject = create_email(namn)
        content = create_email(namn)
        receiver_dyn = email
        yag.send(to=receiver_dyn, subject=subject[0], contents=content[1][0], attachments=content[1][1])
        print(f"Sent mail to {namn} and {receiver_dyn}")




run = False
while run:
    current_time = dt.now().strftime("%H%M")
    if current_time == '1247':
        yag = yagmail.SMTP(user=sender, password="cuayewzipxmbnvfq")
        yag.send(to=receiver, subject=subject, contents=content)
        print("Email sent!")
    time.sleep(60)


