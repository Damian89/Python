# This returns messages in raw html

import imaplib
msrvr = imaplib.IMAP4_SSL('imap.gmail.com',993)
 
unm = 'hdquemada@gmail.com'
pwd = 'pqjqelhgktynrgxo'
msrvr.login(unm,pwd)
 
stat,cnt = msrvr.select('Inbox')

stat, dta = msrvr.fetch(cnt[0],'(UID BODY[TEXT])')

print(dta[0][1])

msrvr.close()
msrvr.logout()
