import imaplib
import email

# http://stackoverflow.com/questions/2792623/reading-and-parsing-email-from-gmail-using-c-c-or-python

inbox = imaplib.IMAP4_SSL('imap.gmail.com',993) # Specify mail server
inbox.login('stocr4tes','5nakeC0ffee') # Login to inbox
inbox.select() # Select inbox for read/write
typ, data = inbox.search(None,'ALL') # Get all messages
for num in data[0].split():
    typ, msgData = inbox.fetch(num, '(RFC822)')
    for responsePart in msgData:
        if(isinstance(responsePart, tuple)):
            msg = email.message_from_bytes(responsePart[1]) # Decode message object
            print(msg['subject'])
            if msg.is_multipart() == True:
                for part in msg.get_payload():
                    if part.get_content_type() == 'text/plain':
                        # Prefer text over html if it is available
                        print(part.get_payload())
                    elif part.get_content_type() == 'text/html':
                        # Need an HTML de-parser
                        print(part.get_payload())
                    elif part.get_content_type() == 'image/jpg':
                        pass # Handle jpg
                    else:
                        pass
            else:
                print("Not multipart")