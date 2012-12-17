import imaplib
import email
# http://stackoverflow.com/questions/2792623/reading-and-parsing-email-from-gmail-using-c-c-or-python

inbox = imaplib.IMAP4_SSL('imap.gmail.com',993) # Specify mail server
inbox.login('stocr4tes','5nakeC0ffee') # Login to inbox
inbox.select() # Select inbox for read/write
typ, data = inbox.search(None,'ALL')
for num in data[0].split():
    typ, msgData = inbox.fetch(num, '(RFC822)')
    for responsePart in msgData:
        if(isinstance(responsePart, tuple)):
            msg = email.message_from_string(responsePart[1])
            print(msg['subject'])