'''
Created on Feb 24, 2013

@author: Daniel
'''
import re

class Password(object):
    '''
    Retrieve password from external file
    '''

    def __init__(self, account, configLocale):
        '''
        Constructor
        Arugments
        1. Identify the account to retrieve a password for
        '''
        self.account = account;
        self.configLocale = configLocale
    
    def getPassword(self):
        if(re.match('^stocr4tes@gmail\.com$', self.account, re.IGNORECASE)):
            file = open(self.configLocale,"r") # Open the file
            configData = file.read() # Read file into variable
            return configData # Print the data
        else:
            return False

#password = Password('stocr4tes@gmail.com', '../../../config.txt')
#text = password.getPassword()
#print(text)