# Designed to hopefully clean my inbox
import imaplib
import email
from email.header import decode_header

# Account Credentials
username = "***"
password = "***"

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)

imap.select('"[Gmail]/All Mail"')
status, messages = imap.search(None, 'BEFORE "30-MAY-2021"')
i = 1
messages = messages[0].split(b' ')

for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    print("Deleting number " + str(i))
    i+=1
    imap.store(mail, "+FLAGS", "\\Deleted")

imap.expunge()
imap.close()
print("Deleted " + str(i) + " messages")
imap.logout()