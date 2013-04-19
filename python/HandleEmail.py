import imaplib      # IMAP tools
import email        # Email object
import re           # Regular expressions
import InsertParser # Parse insert statements
import StocratesDb  # Connect to database
import inspect      # Frame inspector

from errorLog import errorLog
errorLog = errorLog(__file__)
from Password import Password
password = Password('stocr4tes@gmail.com', '../../../config.txt')

import pprint       # Pretty printer (development tool)
pp = pprint.PrettyPrinter(indent=4)

# http://stackoverflow.com/questions/2792623/reading-and-parsing-email-from-gmail-using-c-c-or-python

inbox = imaplib.IMAP4_SSL('imap.gmail.com',993) # Specify mail server
inbox.login('stocr4tes', password.getPassword()) # Login to inbox
inbox.select() # Select inbox for read/write
typ, data = inbox.search(None,'UNSEEN') # Get all unread messages. UNSEEN = unread, seen = read, all = all
for num in data[0].split():
    typ, msgData = inbox.fetch(num, '(BODY.PEEK[])') # Do not mark as read for testing purposes
    #typ, msgData = inbox.fetch(num, '(RFC822)') # Mark as read after reading
    for responsePart in msgData:
        if(isinstance(responsePart, tuple)):
            msg = email.message_from_string(responsePart[1]) # Decode message object
            print(msg['subject'])
            if(re.match('^PREDICTION$', msg['subject'], re.IGNORECASE)):
                if msg.is_multipart() == True:
                    for part in msg.get_payload():
                        if part.get_content_type() == 'text/plain':
                            insert = InsertParser.parseText(part.get_payload())
                            print(insert)
                            try:
                                db = StocratesDb.openDb() # Connect to database
                                cur = db.cursor() # Create a cursor
                                cur.execute(insert) # Execute SQL
                            except Exception, e:
                                #print(e)
                                errorLog.writeErrorLog(str(inspect.getframeinfo(inspect.currentframe())[1]), e)
                            # Prefer text over html if it is available
                            #print("This was text!")
                            #print(part.get_payload())
                        elif part.get_content_type() == 'text/html':
                            pass
                            # Need an HTML de-parser
                            #print("This was HTML!")
                            #print(part.get_payload())
                        elif part.get_content_type() == 'image/jpg':
                            pass
                            #print("This was an image!")
                            # Handle jpg
                        else:
                            pass
                else:
                    print("Not multipart")
            else:
                pass
#inbox.store(num,'+FLAGS','(UNSEEN)') # Mark it as unread again