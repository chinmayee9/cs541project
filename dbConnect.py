#!/usr/bin/python

import MySQLdb
import csv
from datetime import date, timedelta
from getAPIData import CryptoCompareData, CoinMarketCapData


def getCurrencyNames():
    # a = CryptoCompareData()
    # a.getCoinList()
    # currencies = a.coinlist.head(n=1000)
    # currencies = list(currencies['CoinName'].apply(str))

    b = CoinMarketCapData()
    b.getData()
    currencies = b.data
    currencies = currencies[['id', 'market_cap_usd', 'name', 'symbol']]
    currencies.to_csv('./csvFiles/coin_market_data.csv')
    currencies = list(currencies['name'].apply(str))
    with open('./csvFiles/list.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Currency'])
        for c in currencies:
            c = tuple([c])
            writer.writerow(c)
    return currencies


def getContent():
    yesterday = date.today() - timedelta(1)
    yesterday_date = yesterday.strftime('%Y-%m-%d')
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    cursor = db.cursor()
    cursor.execute("select distinct(content) from cryptonews where date like %s;", ("%" + yesterday_date + "%",))
    content = cursor.fetchall()
    db.close()
    return content


def readCurrencies():
    currencies = []
    with open('./csvFiles/list.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for index, row in enumerate(reader):
            if index != 0:
                currencies.append(row)
    return currencies


def getDomains(c_name):
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(link, '/', 3), '://', -1), '/', 1), '?', 1),'www.',-2) as domain, count(*) as frequency from cryptonews where content like %s group by domain order by frequency desc limit 10",
        ("%" + str(c_name) + "%",))
    domains = cursor.fetchall()
    db.close()
    return domains
