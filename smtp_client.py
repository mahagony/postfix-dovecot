import smtplib
from email.message import EmailMessage

smtp_host = 'localhost'
smtp_port = 9025

email_sender = 'pfe@pluton.localdomain'
email_receiver = 'test1@mahagony4.me'

message = EmailMessage()
message['Subject'] = 'test text/plain'
message['From'] = email_sender
message['To'] = email_receiver

text = '''
Hi,
How are you?
Real Python as many great tutorials:
www.realpython.com
'''

message.set_content(text)

with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.send_message(message)
