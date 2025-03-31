
from email.mime.text import MIMEText
import yagmail
from email.mime.multipart import MIMEMultipart

sender = "olov.sigurdson@gmail.com"
receiver = "olov.sigurdson@tietoevry.com"
password = "cuayewzipxmbnvfq"

message = MIMEMultipart()
message['from'] = sender
message['To'] = receiver
message['Subject'] = 'Ett mejl!!'

body = """
<h2>Hi there</h2>
Testar html jag
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)

yag = yagmail.SMTP(user=sender, password="cuayewzipxmbnvfq")
message_text = message.as_string()
print(message_text)
yag.send(to=receiver, subject="Testar!!", contents=body)

