import os

import csv
import yfinance as yf
from datetime import datetime
import pytz

headers = ['Date', 'Stock', 'Price']
filename = '../stockprice.csv'

t = yf.Tickers('msft aapl brk.a meta nvda tsla')

def write_to_excel(rows):
    skip_headers = False
    if os.path.isfile(filename):
        skip_headers = True
    with open (filename, 'a', newline="") as csvfile:
        if skip_headers: 
            csvwriter = csv.writer(csvfile)       
        else:
           csvwriter = csv.writer(csvfile)
           csvwriter.writerow(headers) 
        csvwriter.writerows(rows)

if __name__ == "__main__":
    date_format = datetime.now(pytz.timezone("America/New_York")).strftime("%d/%m/%Y %H:%M:%S")
    print("MSFT current price: " + "$" + str(date_format) + " is $" + str(t.tickers['MSFT'].info['currentPrice']))
    
    rows = [[str(date_format), 'AAPL', "$" + str(t.tickers['AAPL'].info['currentPrice'])],
            [str(date_format), 'META', "$" + str(t.tickers['META'].info['currentPrice'])],
            [str(date_format), 'MSFT', "$" + str(t.tickers['MSFT'].info['currentPrice'])],
            [str(date_format), 'NVDA', "$" + str(t.tickers['NVDA'].info['currentPrice'])],
            [str(date_format), 'TSLA', "$" + str(t.tickers['TSLA'].info['currentPrice'])]]

    write_to_excel(rows)
