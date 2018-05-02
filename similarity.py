import gensim
from dbConnect import getContent, readCurrencies
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import pandas


def getStopWords():
    stop_words = stopwords.words('english')
    common = []
    # common = ['aware', 'voice', 'spots', 'hedge', 'cube', 'tokens', 'token', 'roofs', 'warp', 'castle', 'syndicate',
    #           'zilla', 'can', 'money', 'people', 'burst', 'change', 'cloud', 'coin2', 'cream', 'crown', 'crypto',
    #           'cypher', 'data', 'datum', 'diamond', 'elastic', 'emrald', 'flash', 'flip', 'force', 'franks', 'fusion',
    #           'game', 'gambit', 'gas', 'gems', 'guess', 'guts', 'goldcoin', 'heat', 'horizon', 'hush', 'hyper', 'icon',
    #           'ink', 'ins', 'interstellar', 'ion', 'iota', 'jewels', 'kin', 'life', 'maker', 'metal', 'myriad', 'nano',
    #           'neo', 'neuro', 'network', 'node', 'nexus', 'particle', 'passive', 'photon', 'pillar', 'poet', 'read',
    #           'real', 'version','verify','purpose','consensus','hedge']
    stop_words.extend(common)
    return set(stop_words)


def createSims(content):
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    print type(dictionary)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity('similarity', tf_idf[corpus], num_features=len(dictionary))
    return dictionary, tf_idf, sims


def getSimilarity(query_content, dictionary, tf_idf, sims):
    query_doc = [w.lower() for w in word_tokenize(query_content)]
    query_doc_bow = dictionary.doc2bow(query_doc)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print sims[query_doc_tf_idf]


def getCurrencyPopularity(cloud=False, count=None):
    print "getting content..."
    content_raw = getContent()
    content = [unicode(article[0], errors='ignore') for article in content_raw]
    with open('./csvFiles/content_total.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Content', 'Total'])
        writer.writerow(['Content', len(content)])

    print "getting popularity..."
    currencies = readCurrencies()
    for c in currencies:
        c[0] = c[0].lower()
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(currencies)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    total_currencies = [[index, 0] for index in range(len(currencies))]

    stop_words = getStopWords()

    for article in corpus:
        for currency in article:
            index = currency[0]
            total_currencies[index][1] += 1

    popular_currencies = [currency for currency in total_currencies if
                          currency[1] > 0 and str(currencies[currency[0]][0]).lower() not in stop_words]
    popular_currencies = sorted(popular_currencies, key=lambda x: x[1], reverse=True)
    popularity_list = []
    for currency in popular_currencies:
        popularity_list.append([currencies[currency[0]], currency[1]])
    with open('./csvFiles/popularity_list.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Currency', 'Popularity'])
        for p in popularity_list:
            writer.writerow([p[0][0], p[1]])
    if count:
        return popularity_list[:count]
    else:
        return popularity_list


def readPopularity():
    popularity_list = []
    with open('./csvFiles/popularity_list.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for index, row in enumerate(reader):
            if index != 0:
                row[0] = row[0] + " - " + row[1]
                popularity_list.append(row)
    return popularity_list


def readPopularityAfterRating():
    data = pandas.read_csv('./csvFiles/currency_data.csv')
    data_id = data['id'].tolist()
    data_pop = data['Popularity'].tolist()
    popularity_list = []
    for index, pop in enumerate(data_pop):
        if pop != 0:
            # popularity_list.append([data_id[index]  + " - " + str(int(pop)), str(int(pop))])
            popularity_list.append([data_id[index], int(pop)])
    return popularity_list
