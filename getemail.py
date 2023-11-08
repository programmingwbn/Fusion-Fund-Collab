import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from main import *

sender_email = 'fusionfundtestemail@gmail.com'
sender_password = 'yedf ttry sxpm gzfk'
recipient_email = 'maxwellramone@gmail.com'
subject = 'hello'
message = f'Hi here is a list of our weekly summaries: '

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls() 

    server.login(sender_email, sender_password)

    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("test1")
print('Test')