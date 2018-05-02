import pandas


def getDatabyCurrency(currency=None):
    try:
        data = pandas.read_csv('./csvFiles/currency_data.csv')
        data = data.loc[(data['id'] == currency)]

        marketcap = list(data['market_cap_usd'])[0]
        dominance = list(data['dominance'])[0]
        articles = list(data['Popularity'])[0]
        popularity = list(data['percentPopularity'])[0]
        average = list(data['average'])[0]
        std_dev = list(data['stdDeviation'])[0]
        spread = list(data['spreadAboutMean'])[0]
        kurtosis = list(data['kurtosis'])[0]
        skewness = list(data['skewness'])[0]
        rating = list(data['rating'])[0]
        prices = list(data['90dayClosingPrices'])[0]

        if rating >= 6:
            trusted = 2
        if rating >= 4.5 and rating < 6:
            trusted = 1
        if rating < 4.5:
            trusted = 0

        params = {'marketcap': int(marketcap), 'dominance': dominance, 'articles': articles, 'popularity': popularity,
                  'average': average, 'std_dev': std_dev, 'spread': spread, 'kurtosis': kurtosis, 'skewness': skewness,
                  'rating': rating, 'prices': prices, 'trusted': trusted}
        return params

    except:
        print "Could not fetch data for: ", currency
        return {}
