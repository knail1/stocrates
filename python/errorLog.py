'''
Created on Mar 24, 2013

@author: Daniel
'''

class errorLog(object):
    '''
    Record errors to a file
    '''

    def __init__(self, scriptName):
        '''
        Constructor
        '''
        self.scriptName = scriptName
        import re
        self.errorLog = re.sub('\.[a-zA-Z]+$', '.err', self.scriptName, 0, 0)
        return None
    
    def createErrorLog(self):
        '''
        Create an error log if none exists
        '''
        import os.path
        if(os.path.isfile(self.errorLog)): # If the error log already exists
            return True # It has been created before
        else:
            # Create it
            import datetime # Date and time functions
            errorFile = open(self.errorLog, 'w') # Open for writing
            errorFile.write("{:28}{:16}{}".format('Date', 'Line Number', 'Error Message')) # Write the header
            errorFile.write("\n{:28}{:16}{}".format(str(datetime.datetime.now()), '-', 'Error log created.'))
            errorFile.close()
            return True
        
    def writeErrorLog(self, lineNum, errorMsg):
        '''
        Write a an error message to the error log
        '''
        import datetime # Date and time functions
        self.createErrorLog() # Ensure the error log is created
        errorFile = open(self.errorLog, 'a') # Open for appending
        errorFile.write("\n{:28}{:16}{}".format(str(datetime.datetime.now()), lineNum, errorMsg)) # Record the error message
        errorFile.close()
        return True