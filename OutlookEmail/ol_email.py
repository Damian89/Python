# This script is based on the YouTube video https://youtu.be/bXRYJEKjqIM, but modified with what I've learned from
# other videos, especially to have information that I can change put into a different file, called "emlinfo.py"

# This script works.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import olemlinfo

email_user = olemlinfo.EMAIL_ADDRESS
email_send = olemlinfo.EMAIL_SEND

subject = olemlinfo.SUBJECT

msg = MIMEMultipart()
msg['From'] = 'Hector Quemada <hector.quemada@wmich.edu>'
msg['To'] = ', '.join(email_send)
msg['Subject'] = subject

body = olemlinfo.BODY
msg.attach(MIMEText(body,'plain'))











text = msg.as_string()
server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(olemlinfo.EMAIL_ADDRESS,olemlinfo.PASSWORD)

server.sendmail(email_user,email_send,text)

server.quit()
print('Email sent!')
