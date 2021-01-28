import requests
import pandas as pd
import json
import os
import dotenv
import matplotlib.pyplot as plt
dotenv.load_dotenv(verbose=True)
key = os.getenv('VantageAlphaApi')
#print(key)

# key = 
function = 'TIME_SERIES_INTRADAY'
sym = 'GME'
interval = '5min'
link = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + sym + '&interval=' + interval + '&apikey=' + key

res = requests.get(link)

data_json = res.json()

#print(data_json)
#data = json.loads(data_json)
#df = pd.json_normalize(data['results'])
# df = pd.read_json(data_json)

test = data_json['Time Series (5min)']
# print(test)

for i in test:
    str = i
    print(str)
    print(test[str])

# print(test['2021-01-27 09:35:00'])
df = pd.DataFrame(test).transpose()
df.columns=['open','high','low','close','volume']
print(df.head())

print(df['close'])
# df['close'].plot()

#print(req.json())

#print(data.head())
