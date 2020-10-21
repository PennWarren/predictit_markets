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
                          ("Arkansas", 6597),
                          ("California", 6611),
                          ("Colorado", 5605),
                          ("Connecticut", 6587),
                          ("D.C.", 6644),
                          ("Delaware", 6636),
                          ("Florida", 5544),
                          ("Georgia", 5604),
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
                          ("New Mexico", 6573),
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

senate_race_list = (("Alabama", 6183),
                    ("Alaska", 6688),
                    ("Arizona (Special)", 5809),
                    ("Arkansas", 6827),
                    ("Colorado", 5810),
                    ("Delaware", 6808),
                    ("Georgia (Regular)", 6651),
                    ("Georgia (Special)", 6567),
                    ("Idaho", 6810),
                    ("Illinois", 6830),
                    ("Iowa", 6648),
                    ("Kansas", 5781),
                    ("Kentucky", 6575),
                    ("Louisiana", 6813),
                    ("Maine", 5811),
                    ("Massachusetts", 6840),
                    ("Michigan", 6576),
                    ("Minnesota", 6761),
                    ("Mississippi", 6839),
                    ("Montana", 6568),
                    ("Nebraska", 6832),
                    ("New Hampshire", 6795),
                    ("New Jersey", 6801),
                    ("New Mexico", 6752),
                    ("North Carolina", 5808),
                    ("Oklahoma", 6841),
                    ("Oregon", 6786),
                    ("Rhode Island", 6842),
                    ("South Carolina", 6706),
                    ("South Dakota", 6826),
                    ("Tennessee", 6792),
                    ("Texas", 6788),
                    ("Virginia", 6821),
                    ("West Virginia", 6837),
                    ("Wyoming", 6797))


def get_ninety_days_presidential():
    save_file = 'PredictIt/Presidential/predictit_presidential_' + str(datetime.date.today())
    with open(save_file, 'w+', newline='') as f:
        count = 0

        for i, race in enumerate(electoral_college_list):

            time.sleep(2.25)
            market_data = data(race[0], race[1])

            print(i)
            if (i == 0):
                market_data.to_csv(f, header=True)
            else:
                market_data.to_csv(f, header=False)

def get_ninety_days_senate():
    save_file = 'PredictIt/Senate/predictit_senate_' + str(datetime.date.today())
    with open(save_file, 'w+', newline='') as f:
        count = 0

        for i, race in enumerate(senate_race_list):

            time.sleep(2.25)
            market_data = data(race[0], race[1])

            print(i)
            if (i == 0):
                market_data.to_csv(f, header=True)
            else:
                market_data.to_csv(f, header=False)


if __name__ == '__main__':
    get_ninety_days_presidential()
    get_ninety_days_senate()