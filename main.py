#import logging
#import logging.handlers
#import os

#import requests
import csv
import yfinance as yf
from datetime import datetime

fields = ['Date', 'Stock', 'Price']
filename = 'ctockprice.csv'

t = yf.Tickers('msft aapl brk.a meta nvda tsla')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger_file_handler = logging.handlers.RotatingFileHandler(
#     "status.log",
#     maxBytes=1024 * 1024,
#     backupCount=1,
#     encoding="utf8",
# )
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logger_file_handler.setFormatter(formatter)
# logger.addHandler(logger_file_handler)

# try:
#     SOME_SECRET = os.environ["SOME_SECRET"]
# except KeyError:
#     SOME_SECRET = "Token not available!"
#     #logger.info("Token not available!")
#     #raise


if __name__ == "__main__":
    print("MSFT current price: " + str(datetime.now()) + " is $" + str(t.tickers['MSFT'].info['currentPrice']))
    rows = [[str(datetime.now()), 'AAPL', str(t.tickers['AAPL'].info['currentPrice'])],

            [str(datetime.now()), 'META', str(t.tickers['META'].info['currentPrice'])],
            [str(datetime.now()), 'MSFT', str(t.tickers['MSFT'].info['currentPrice'])],
            [str(datetime.now()), 'NVDA', str(t.tickers['NVDA'].info['currentPrice'])],
            [str(datetime.now()), 'TSLA', str(t.tickers['TSLA'].info['currentPrice'])]]

    with open (filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    #logger.info(f"Token value: {SOME_SECRET}")
    # print("check")
    # r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    # if r.status_code == 200:
    #     data = r.json()
    #     temperature = data["forecast"]["temp"]
    #     print("check2 " + str(temperature))
    #     print("yahoo" + str(t.tickers['MSFT'].info))
    #     logger.info(f'Weather in Berlin: {temperature}')