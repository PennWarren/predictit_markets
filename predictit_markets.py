# df creator using predictits csv downloads that are available
import pandas as pd
import numpy as np
import datetime
import time
import csv


def data(name, number):
    # Possible times: 24h, 7d, 30d, 90d
    time = '90d'
    url = 'https://www.predictit.org/Resource/DownloadMarketChartData?marketid=' + str(number) + '&timespan=' + str(
        time)
    df = pd.read_csv(url)

    # Creating array for market name column
    name_column = np.empty(df.shape[0], dtype='U20')
    name_column.fill(name)

    # Append the location column
    df.insert(0, "Region", name_column)
    return df


def market_name(market):
    # this may not be the best way to do it, but it worked pretty well for me 
    df = pd.read_json('https://www.predictit.org/api/marketdata/markets/' + str(market))
    # sets the market to a string and returns it. 
    text = str(df['name'][0])
    return text


electoral_college_list = (("Alabama", 6625),
                          ("Alaska", 6591),
                          ("Arizona", 5596),
                          ("California", 6611),
                          ("Colorado", 5605),
                          ("Connecticut", 6587),
                          ("D.C.", 6644),
                          ("Florida", 5544),
                          ("Georgia", 6651),
                          ("Hawaii", 6631),
                          ("Idaho", 6623),
                          ("Illinois", 6613),
                          ("Indiana", 6572),
                          ("Iowa", 5603),
                          ("Kansas", 6627),
                          ("Kentucky", 6592),
                          ("Louisiana", 6617),
                          ("Maine", 6571),
                          ("Maine-01", 6647),
                          ("Maine-02", 6190),
                          ("Maryland", 6593),
                          ("Massachusetts", 6596),
                          ("Michigan", 5545),
                          ("Minnesota", 5597),
                          ("Mississippi", 6628),
                          ("Missouri", 6581),
                          ("Montana", 6606),
                          ("Nebraska", 6624),
                          ("Nebraska-01", 6645),
                          ("Nebraska-02", 6608),
                          ("Nebraska-03", 6646),
                          ("Nevada", 5601),
                          ("New Hampshire", 6580),
                          ("New Jersey", 6580),
                          ("New Mexico", 6752),
                          ("New York", 6612),
                          ("North Carolina", 5599),
                          ("North Dakota", 6637),
                          ("Ohio", 5600),
                          ("Oklahoma", 6616),
                          ("Oregon", 6582),
                          ("Pennsylvania", 5543),
                          ("Rhode Island", 6629),
                          ("South Carolina", 6609),
                          ("South Dakota", 6638),
                          ("Tennessee", 6586),
                          ("Texas", 5798),
                          ("Utah", 6585),
                          ("Vermont", 6633),
                          ("Virginia", 5602),
                          ("Washington", 6598),
                          ("West Virginia", 6615),
                          ("Wisconsin", 5542),
                          ("Wyoming", 6632))


def get_ninety_days():
    save_file = 'predictit_presidential' + str(datetime.date.today())
    with open(save_file, 'w+', newline='') as f:
        count = 0

        for i, race in enumerate(electoral_college_list):

            time.sleep(2.5)
            market_data = data(race[0], race[1])

            print(i)
            if (i == 0):
                market_data.to_csv(f, header=True)
            else:
                market_data.to_csv(f, header=False)