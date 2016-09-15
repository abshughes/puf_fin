from yahoo_finance import Share
import json
import pandas as pd
from pandas.io.json import json_normalize

from urllib2 import Request, urlopen
import json


yahoo = Share('YHOO')
#print yahoo.get_open()
#print yahoo.get_price()
#print yahoo.get_trade_datetime()
#print yahoo.get_historical('2014-04-25', '2014-04-29')


##df=pd.read_json(yahoo.splitlines())
#print "this is pandas now"

list_of_rates=yahoo.get_historical('2014-04-25', '2016-04-28')
print list_of_rates
print pd.DataFrame(list_of_rates)