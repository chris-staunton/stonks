import requests
import pandas as pd
import json
import os
import csv
import dotenv
import matplotlib.pyplot as plt
dotenv.load_dotenv(verbose=True)
key = os.getenv('VantageAlphaApi')
#print(key)

plt.rcParams.update({'font.size': 8})

# key = 
mode = "INTRADAY_EXTENDED"
function = 'TIME_SERIES_' + mode
sym = 'GME'
interval = '30min'
link = 'https://www.alphavantage.co/query?function=' + function + '&symbol=' + sym + '&interval=' + interval + '&apikey=' + key

res = requests.get(link)

if(res.status_code == 200):
    if(mode == "INTRADAY"):
        data_json = res.json()

        #print(data_json)
        #data = json.loads(data_json)
        #df = pd.json_normalize(data['results'])
        # df = pd.read_json(data_json)

        test = data_json['Time Series (5min)']
        # print(test)
        # str = ''
        # for i in test:
        #     str += i
        #     print(str)
        #     print(test[str])

        # print(test[0])

        # print(test['2021-01-27 09:35:00'])
        df = pd.DataFrame(test).transpose()
        df.columns=['open','high','low','close','volume']
        #df.index_col('date')
        print(df.head())
        #df.plot()
        # print(df['close'])
        # df['close'].plot()
        df.index.name = 'date'
        print(df.index)
        #print(req.json())

        #print(data.head())
        df = df.drop('volume', 1)
        print(df.head())
        df=df.astype(float)
        # plt.figure()
        df.plot()
        plt.show()

        print(df.plot())
    elif(mode == "INTRADAY_EXTENDED"):
        print("extended")
        #df = pd.read_csv(res)
        #df.head()
        print(res)
        # cr = csv.reader(res)
        # for row in cr:
        #     print(row)
        # #print(cr)

        df = pd.read_csv(link, index_col= False)
        df = df.drop('volume', 1)
        df = df.set_index('time')
        df = df[::-1]
        print(df.head())

        df.plot()
        plt.show()

    else:
        print("error")
else:
    print("api error")