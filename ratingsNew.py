from scipy import stats
import numpy as np
from scipy.stats import kurtosis, skew
from getAPIData import CryptoCompareData, CoinMarketCapData
import pandas


def getSpread(prices, std_dev, avg):
    total = len(prices)
    count = 0
    for price in prices:
        if abs(price - avg) <= std_dev:
            count += 1
    return ((count / float(total)) * 100)


def getRating(dominance, popularity, kutosis, skewness, spread):
    rating = 0
    rating += dominance
    rating += popularity * 10
    if kutosis <= 0:
        rating += 100
    elif kutosis > 0 and kutosis <= 1:
        rating += (1 - kutosis) * 100
    else:
        rating += 0
    if skewness < 0:
        rating += 0
    elif skewness > 1:
        rating += 100
    else:
        rating += skewness * 100
    if spread <= 68.3:
        rating += 100
    else:
        rating += ((spread - 68.3) / 68.3) * 100
    rating = (rating / 400) * 10
    return rating


def calculateRating():
    average = []
    standard_deviation = []
    ratio = []
    kurtosis_measure = []
    skewness = []
    currency_prices = []
    rating = []

    a = CryptoCompareData()
    a.getCoinList()

    b = CoinMarketCapData()
    b.getGlobalData()
    total_market_capital = b.globaldata['total_market_cap_usd'].tolist()
    total_market_capital = total_market_capital[0]

    currency_data = pandas.read_csv('./csvFiles/coin_market_data.csv')
    currency_data['dominance'] = currency_data['market_cap_usd'].div(total_market_capital).mul(100)
    temp_name_list = currency_data['id'].tolist()
    temp_symbol_list = currency_data['symbol'].tolist()
    temp_dominance_list = currency_data['dominance'].tolist()

    popularity_data = pandas.read_csv('./csvFiles/popularity_list.csv')
    currency_data = currency_data.set_index('id').join(popularity_data.set_index('Currency')).fillna(0)

    total_articles = pandas.read_csv('./csvFiles/content_total.csv')
    total_articles = total_articles.loc[(total_articles['Content'] == 'Content')]
    total_articles = list(total_articles['Total'])[0]
    currency_data['percentPopularity'] = currency_data['Popularity'].div(total_articles).mul(100)
    temp_popularity_list = currency_data['percentPopularity'].tolist()

    inaccessible_symbols = []
    for index, symbol in enumerate(temp_symbol_list):
        try:
            closing_data = a.getDataByDays(currency=symbol)
            prices = closing_data['close'].tolist()
            avg = np.mean(prices)
            std_dev = np.std(prices)
            kurto = kurtosis(prices)
            ske = skew(prices)
            spread = getSpread(prices, std_dev, avg)
            currency_rating = getRating(temp_dominance_list[index], temp_popularity_list[index], kurto, ske, spread)

            average.append(avg)
            standard_deviation.append(std_dev)
            ratio.append(spread)
            kurtosis_measure.append(kurto)
            skewness.append(ske)
            currency_prices.append(prices)
            rating.append(currency_rating)

        except:
            print "Couldn't get data for: " + symbol
            inaccessible_symbols.append(symbol)
            continue

    for symbol in inaccessible_symbols:
        for index, row in currency_data.iterrows():
            if row['symbol'] == symbol:
                currency_data.drop(index, inplace=True)

    currency_data['average'] = average
    currency_data['stdDeviation'] = standard_deviation
    currency_data['spreadAboutMean'] = ratio
    currency_data['kurtosis'] = kurtosis_measure
    currency_data['skewness'] = skewness
    currency_data['rating'] = rating
    currency_data['90dayClosingPrices'] = currency_prices

    currency_data.to_csv('./csvFiles/currency_data.csv')
