import requests
import os
import dotenv
dotenv.load_dotenv(verbose=True)
key = os.getenv('VantageAlphaApi')
#print(key)

# key = 
function = 'TIME_SERIES_INTRADAY'
sym = 'IBM'
interval = '5min'
link = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + sym + '&interval=' + interval + '&apikey=' + key

req = requests.get(link)

print(req.json())

