from investopedia_api import InvestopediaApi, TradeExceedsMaxSharesException
import json
import datetime

credentials = {}
with open('credentials.json') as ifh:
    credentials = json.load(ifh)
# look at credentials_example.json
# credentials = {"username": "you@example.org", "password": "yourpassword" }
client = InvestopediaApi(credentials)

p = client.portfolio
print("account value: %s" % p.account_value)
print("cash: %s" % p.cash)
print("buying power: %s" % p.buying_power)
print("annual return pct: %s" % p.annual_return_pct)

# get a quote
quote = client.get_stock_quote('GOOG')
print(quote.__dict__)
    
# construct a trade (see trade_common.py and stock_trade.py for a hint)
trade1 = client.StockTrade(symbol='GOOG', quantity=10, trade_type='buy',
                           order_type='market', duration='good_till_cancelled', send_email=True)
# validate the trade
trade_info = trade1.validate()
print(trade_info)

# change the trade to a day order
trade1.duration = 'day_order'
# Another way to change the trade to a day order
trade1.duration = client.TradeProperties.Duration.DAY_ORDER()

# make it a limit order
trade1.order_type = 'limit 20.00'
# alternate way
trade1.order_type = client.TradeProperties.OrderType.LIMIT(20.00)

# validate it, see changes:
trade_info = trade1.validate()
if trade1.validated:
    print(trade_info)
    trade1.execute()
