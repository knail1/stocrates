'''
Created on Mar 4, 2013

@author: Daniel
'''


def openDb():
    '''
    Open the connection to the database
    '''
    import MySQLdb.converters
    dictConv = MySQLdb.converters.conversions
    dbStocrates = MySQLdb.connect(host='stocrates.dnsdynamic.com',
                                  user='root',
                                  db='stocrates',
                                  conv=dictConv)
    return dbStocrates