import requests
import json
import time
from pandas import *


class CryptoCompareData(object):
    def __init__(self, baseurl='https://min-api.cryptocompare.com/data/', params={}):
        self.baseurl = baseurl
        self.params = {'tsym': 'USD', 'toTS': time.time(), 'extraParams': 'CryptoSales'}
        self.coinlist = DataFrame()

    def callAPI(self, url):
        try:
            req = requests.get(url)
            response = req.json()
            return response
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getCoinList(self):
        try:
            url = self.baseurl + 'all/coinlist'
            response = self.callAPI(url)
            coindata = []
            for coin, details in response['Data'].iteritems():
                coindata.append(details)
            df = DataFrame(coindata)
            df['SortOrder'] = to_numeric(df['SortOrder'])
            df.sort_values(by='SortOrder', ascending=True, inplace=True)
            self.coinlist = df
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getDataByDays(self, days=90, aggregate=1, currency='BTC'):
        try:
            self.params['aggregate'] = aggregate
            self.params['limit'] = days
            self.toTS = int(time.time())
            self.params['fsym'] = currency
            qstring = '?allData'

            for p, value in self.params.iteritems():
                qstring += '&' + str(p) + '=' + str(value)

            url = self.baseurl + 'histoday' + qstring
            response = self.callAPI(url)
            df = DataFrame(response['Data'])
            return df
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getDataByHour(self, hours=24, aggregate=1, currency='BTC'):
        try:
            self.params['aggregate'] = aggregate
            self.params['limit'] = hours
            self.toTS = int(time.time())
            self.params['fsym'] = currency
            qstring = '?allData'

            for p, value in self.params.iteritems():
                qstring += '&' + str(p) + '=' + str(value)

            url = self.baseurl + 'histohour' + qstring
            response = self.callAPI(url)
            df = DataFrame(response['Data'])
            return df
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getSocialStats(self, currency='bitcoin'):
        try:
            url = 'https://www.cryptocompare.com/api/data/socialstats/?id='
            df = self.coinlist.loc[(self.coinlist['Name'] == currency) | (self.coinlist['Symbol'] == currency) | (
                    self.coinlist['CoinName'].str.lower() == currency)]
            id = list(df['Id'])[0]
            url = url + str(id)
            response = self.callAPI(url)
            twitter = DataFrame(response['Data']['Twitter'], index=[0])
            reddit = DataFrame(response['Data']['Reddit'], index=[0])
            facebook = DataFrame(response['Data']['Facebook'], index=[0])
            return twitter, reddit, facebook
        except:
            print "An unexpected error occurred. Data could not be fetched."

    # def getAverageData(self, days=30, currency='BTC'):
    #     try:
    #         df = self.getDataByDays(days=days, aggregate=1, currency=currency)
    #         times = list(df['time'])
    #         url = self.baseurl + 'dayAvg?fsym=' + currency + '&tsym=USD&avgType=HourVWAP&extraParams=cryptotales&toTs='
    #         avgPrices = []
    #         for time in times:
    #             response = self.callAPI(url + str(time))
    #             avgPrices.append(response['USD'])
    #         df['AvgPrice'] = avgPrices
    #         return df
    #     except:
    #         print "An unexpected error occurred. Data could not be fetched."


class CoinMarketCapData(object):
    def __init__(self, baseurl='https://api.coinmarketcap.com/v1/'):
        self.baseurl = baseurl
        self.data = DataFrame()
        self.globaldata = DataFrame()

    def callAPI(self, url):
        try:
            req = requests.get(url)
            response = req.json()
            return response
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getData(self):
        try:
            url = self.baseurl + 'ticker/'
            response = self.callAPI(url)
            self.data = DataFrame(response)
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getGlobalData(self):
        try:
            url = self.baseurl + 'global/'
            response = self.callAPI(url)
            self.globaldata = DataFrame(response, index=[0])
        except:
            print "An unexpected error occurred. Data could not be fetched."

    # Pass coin name
    # def getDataForCurrency(self, id=None):
    #     try:
    #         if id:
    #             url = self.baseurl + 'ticker/' + id
    #             # print url
    #             df = self.callAPI(url)
    #             return DataFrame(df, index=[0])
    #     except:
    #         print "An unexpected error occurred. Data could not be fetched."

    def getDataForCurrency(self, id=None):
        try:
            if id:
                df = self.data.loc[(self.data['id'] == id) | (self.data['symbol'] == id)]
                return df
        except:
            print "An unexpected error occurred. Data could not be fetched."

# if __name__ == '__main__':
#     a = CryptoCompareData()
#     a.getCoinList()
#     a.getDataByDays()
#     a.getDataByHour()
#     a.getSocialStats()
#     a.getAverageData()
#     twitter, reddit, facebook = a.getSocialStats()
#     print facebook
#     twitter, reddit, facebook = a.getSocialStats(currency='ETH')
#     print reddit
#
#     b = CoinMarketCapData()
# #     b.getGlobalData()
# #     global_data = b.globaldata
# #     print global_data
# #     b.getData()
#     symbol_data = b.getDataForCurrency('diamond')
#     print symbol_data
