from scipy import stats
import numpy as np
from scipy.stats import kurtosis, skew
from getAPIData import CryptoCompareData, CoinMarketCapData
import pandas


def getSlope(volume):
    x = list(range(len(volume)))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, volume)
    return slope, intercept


def getSpread(prices, std_dev, avg):
    total = len(prices)
    count = 0
    for price in prices:
        if abs(price - avg) <= std_dev:
            count += 1
    return ((count / float(total)) * 100)


def getRating(popularity, kutosis, skewness, spread):
    rating = 0
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
    volume_slope_column = []
    volume_intercept_column = []
    average = []
    standard_deviation = []
    ratio = []
    kurtosis_measure = []
    skewness = []
    rating = []
    currency_prices = []
    currency_volumes = []
    market_capital = []
    capital_dominance = []
    rating = []
    popularity = []
    currency_articles = []

    a = CryptoCompareData()
    a.getCoinList()
    currency_data = a.coinlist.head(n=1000)
    currency_data = currency_data[['SortOrder', 'Symbol', 'Name', 'CoinName', 'Id', 'FullName']]
    temp_name_list = currency_data['CoinName'].tolist()
    temp_symbol_list = currency_data['Symbol'].tolist()

    b = CoinMarketCapData()
    b.getGlobalData()
    total_market_capital = b.globaldata['total_market_cap_usd'].tolist()
    total_market_capital = total_market_capital[0]
    b.getData()
    currency_marketcapital = b.data

    popularity_data = pandas.read_csv('./csvFiles/popularity_list.csv')
    popularity_name_list = popularity_data['Currency'].tolist()
    total_articles = pandas.read_csv('./csvFiles/content_total.csv')
    total_articles = total_articles.loc[(total_articles['Content'] == 'Content')]
    total_articles = list(total_articles['Total'])
    total_articles = total_articles[0]

    inaccessible_symbols = []

    for index, symbol in enumerate(temp_symbol_list):
        try:
            closing_data = a.getDataByDays(currency=symbol)
            prices = closing_data['close'].tolist()
            volumes = closing_data['volumefrom'].tolist()

            vol_slope, vol_intercept = getSlope(volumes)
            avg = np.mean(prices)
            std_dev = np.std(prices)
            kurto = kurtosis(prices)
            ske = skew(prices)

            try:
                # symbol_marketcapital = b.getDataForCurrency(id=str(temp_name_list[index]).lower())
                symbol_marketcapital = currency_marketcapital.loc[(currency_marketcapital['symbol'] == str(symbol))]
                symbol_marketcapital = list(symbol_marketcapital['market_cap_usd'])
                symbol_marketcapital = symbol_marketcapital[0]
            except:
                symbol_marketcapital = 0
            market_c = float(symbol_marketcapital) / float(total_market_capital) * 100

            currency = temp_name_list[index].lower()
            if currency in popularity_name_list:
                pop = popularity_data.loc[(popularity_data['Currency'] == str(currency))]
                pop = list(pop['Popularity'])
                pop = pop[0]
            else:
                pop = 0
            percent_pop = (pop / float(total_articles)) * 100

            spread = getSpread(prices, std_dev, avg)
            currency_rating = getRating(percent_pop, kurto, ske, spread)

            volume_slope_column.append(vol_slope)
            volume_intercept_column.append(vol_intercept)
            average.append(avg)
            standard_deviation.append(std_dev)
            ratio.append(spread)
            kurtosis_measure.append(kurto)
            skewness.append(ske)
            currency_prices.append(prices)
            currency_volumes.append(volumes)
            market_capital.append(symbol_marketcapital)
            capital_dominance.append(market_c)
            currency_articles.append(pop)
            popularity.append(percent_pop)
            rating.append(currency_rating)

        except:
            print "Couldn't get data for: " + symbol
            inaccessible_symbols.append(symbol)
            continue

    for symbol in inaccessible_symbols:
        for index, row in currency_data.iterrows():
            if row['Symbol'] == symbol:
                currency_data.drop(index, inplace=True)

    currency_data['marketCapital'] = market_capital
    currency_data['currencyDominance'] = capital_dominance
    currency_data['newsArticles'] = currency_articles
    currency_data['percentPopularity'] = popularity
    currency_data['volumeSlope'] = volume_slope_column
    currency_data['volumeIntercept'] = volume_intercept_column
    currency_data['average'] = average
    currency_data['stdDeviation'] = standard_deviation
    currency_data['spreadAboutMean'] = ratio
    currency_data['kurtosis'] = kurtosis_measure
    currency_data['skewness'] = skewness
    currency_data['rating'] = rating
    currency_data['90dayClosingPrices'] = currency_prices
    currency_data['90dayVolumes'] = currency_volumes

    currency_data.to_csv('./csvFiles/currency_data.csv')
