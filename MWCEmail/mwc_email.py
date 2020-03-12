# This script is based on the YouTube video https://youtu.be/bXRYJEKjqIM, but modified with what I've learned from
# other videos, especially to have information that I can change put into a different file, called "emlinfo.py"

# This script works.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import emlinfo

email_user = emlinfo.EMAIL_ADDRESS
email_send = emlinfo.EMAIL_SEND

subject = emlinfo.SUBJECT

msg = MIMEMultipart()
msg['From'] = 'Hector Quemada <email_user>'
msg['To'] = ', '.join(email_send)
msg['Subject'] = subject

body = emlinfo.BODY
msg.attach(MIMEText(body,'plain'))











text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(emlinfo.EMAIL_ADDRESS,emlinfo.PASSWORD)

server.sendmail(email_user,email_send,text)

server.quit()
print('Email sent!')
                    
