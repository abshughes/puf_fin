from yahoo_finance import Share
yahoo = Share('YHOO')
print yahoo.get_open()
print yahoo.get_price()
print yahoo.get_trade_datetime()
print yahoo.get_historical('2014-04-25', '2014-04-29')