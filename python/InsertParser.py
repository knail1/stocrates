'''
Created on Feb 26, 2013

@author: Daniel
'''
import shlex # Simple lexical analyzer
import re # Reguler expressions
#class InsertParser(object):
#    '''
#    Used this class to prep an e-mail for insertion into
#    '''
def parseText(text):
    sqlStart = 'INSERT INTO analyst ('
    sqlEnd = 'VALUES ('
    arrInfo = shlex.split(text)
    for item in arrInfo:
        arg, equalSign, value = item.partition('=')
        if(re.match('^first$', arg, re.IGNORECASE)):
            sqlStart += 'first_name,'
            sqlEnd += '"' + value + '",'
        elif(re.match('^last$', arg, re.IGNORECASE)):
            sqlStart += 'last_name,'
            sqlEnd += '"' + value + '",'
        elif(re.match('^description$', arg, re.IGNORECASE)):
            sqlStart += 'description,'
            sqlEnd += '"' + value + '",'
        elif(re.match('^firm$', arg, re.IGNORECASE)):
            sqlStart += 'firm,'
            sqlEnd += '"' + value + '",'
        elif(re.match('^(rum|revenue_under_management)$', arg, re.IGNORECASE)):
            sqlStart += 'revenue_under_mgmt,'
            value.replace(',','')
            sqlEnd += value + ','
        else:
            pass
    sqlStart = sqlStart[:-1] # Chop off the last comma
    sqlEnd = sqlEnd[:-1] # Chop off the last comma
    return sqlStart + ') ' + sqlEnd + ')'
    
        