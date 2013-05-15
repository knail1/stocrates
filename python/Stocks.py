'''
Created on Apr 30, 2013

@author: Daniel
'''
import urllib2
import datetime
import re
import decimal

class Stock(object):
    '''
    classdocs
    '''

    def __init__(self, stockSymbol):
        '''
        Create an object from a stock symbol
        '''
        self.stockSymbol = stockSymbol
        return None
    
    def price(self, date = None):
        '''
        Arguments: 1
        1. Optional. Date for stock price in format YYYY-MM-DD. Default = current date
        Returns: Price of stock for the date provided or the first date previous with a price
        '''
        if(date == None): # User did not pass an date
            date = datetime.datetime.now() # Use the current date
        else: # User passed a date
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
        attempts = 0 # Only attempt to get the current stock price 
        while(attempts < 10): # Only attempt to get the current stock price for a finite number of attempts to avoid an infinite loop
            a = d = date.month - 1 # Month. Yahoo stores months as 0-11 so subtract 1
            b = e = date.day # Day
            c = f = date.year # Year
            url = "http://ichart.finance.yahoo.com/table.csv?s=CSCO&a={0:02d}&b={1}&c={2}&d={3:02d}&e={4}&f={5}&g=d&ignore=.csv".format(a, b, c, d, e, f)
            response = urllib2.urlopen(url) # Retrieve the prices
            text = response.read() # Read the csv
            closeIndex = None # Column index of the close price
            closePrice = None # Close price
            r = 0 # Row
            for csv in text.split('\n'): # For each row in the csv
                i = 0 # Item index
                for item in csv.split(','): # For each item in the row
                    if(r == 0): # Header row
                        if(re.match('^(close)$', item, re.IGNORECASE)):
                            closeIndex = i # Column number of close price
                    else: # First data row
                        if(len(item) == 0): # If the first cell in line 2 is empty
                            # No data was found in it, meaning there is no price for this date
                            date = date-datetime.timedelta(days=1) # Subtract 1 from the current date
                            continue # Move on the to the next iteration
                        if(closeIndex == i):
                            closePrice = decimal.Decimal(item)
                            return closePrice
                    i += 1
                r += 1
            attempts += 1
   
        