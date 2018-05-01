import pandas
from dbConnect import getDomains


def getDatabyCurrency(currency=None):
    try:
        data = pandas.read_csv('./csvFiles/currency_data.csv')
        data = data.loc[(data['CoinName'] == currency.capitalize())]

        marketcap = list(data['marketCapital'])[0]
        dominance = list(data['currencyDominance'])[0]
        articles = list(data['newsArticles'])[0]
        popularity = list(data['percentPopularity'])[0]
        volslope = list(data['volumeSlope'])[0]
        volintercept = list(data['volumeIntercept'])[0]
        average = list(data['average'])[0]
        std_dev = list(data['stdDeviation'])[0]
        spread = list(data['spreadAboutMean'])[0]
        kurtosis = list(data['kurtosis'])[0]
        skewness = list(data['skewness'])[0]
        rating = list(data['rating'])[0]
        prices = list(data['90dayClosingPrices'])[0]
        volumes = list(data['90dayVolumes'])[0]
        # domains = getDomains(currency)

        if rating > 5.7:
            trusted = 2
        if rating > 3.5 and rating <= 5.7:
            trusted = 1
        if rating <= 3.5:
            trusted = 0


        params = {'marketcap': int(marketcap), 'dominance': dominance, 'articles': articles, 'popularity': popularity,
                  'volslope': volslope, 'volintercept': volintercept, 'average': average, 'std_dev': std_dev,
                  'spread': spread, 'kurtosis': kurtosis, 'skewness': skewness, 'rating': rating, 'prices': prices,
                  'volumes': volumes, 'domains':[], 'trusted' : trusted}
        return params
    except:
        print "Could not fetch data for: ", currency
        return {}
