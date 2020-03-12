# Simple script to send email using smtplib module.
#
# I had to generate another app password on Google.
# This was to allow me to send emails from the old MacBook Pro.
# instead of my login password for hdquemada@gmail.com
# This works

import smtplib

TO = 'hdquemada@yahoo.com'
SUBJECT = 'Sending email using smtplib in Python'
TEXT = 'This is a test message.'

# Gmail Credentials
sender = 'hdquemada@gmail.com'
passwd = 'kxeuzaxciojzqfan'

# Create connection to gmail service
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender, passwd)

BODY = '\r\n' .join([
        'To: %s' % TO,
        'From: Hector Quemada <%s>' % sender,
        'Subject: %s' % SUBJECT,
        ' ',
        TEXT])

try:
    server.sendmail(sender, [TO], BODY)
    print('Email sent')
except:
    print('Error sending email')

server.quit()
