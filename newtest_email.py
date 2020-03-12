# YouTube Video: https://www.youtube.com/watch?v=mP_Ln-Z9-XY
# A different script to send emails
# This references the file "emlinfo.py'
# This script works

import smtplib

import emlinfo


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(emlinfo.EMAIL_ADDRESS, emlinfo.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(emlinfo.EMAIL_ADDRESS, emlinfo.EMAIL_SEND, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = emlinfo.SUBJECT
msg = emlinfo.BODY

send_email(subject, msg)
