from dbConnect import getCurrencyNames
from similarity import getCurrencyPopularity
from ratingsNew import calculateRating

print 'running getCurrencyNames...'
getCurrencyNames()
print 'running getCurrencyPopularity...'
getCurrencyPopularity()
print 'running calculateRating...'
calculateRating()
