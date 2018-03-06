# For this example, we're going to write a simple momentum script.  
# When the stock goes up quickly, we're going to buy; 
# when it goes down we're going to sell.  
# Hopefully we'll ride the waves.

# To run an algorithm in Quantopian, you need two functions: 
# initialize and handle_data
from operator import itemgetter

def initialize(context):
  context.topMom = 1
context.rebal_int = 3
context.lookback = 250
set_symbol_lookup_date('2015-01-01')
#context.stocks = symbols('SPY', 'VOO', 'IVV')
#context.stocks = symbols('XLF', 'XLE', 'XLU', 'XLK', 'XLB', 'XLP', 'XLY', 'XLI', 'XLV', 'BIL')
#context.stocks = symbols('SPY', 'VEA', 'BIL')
context.stocks = symbols('SPY', 'EFA', 'BND', 'VNQ', 'GSG', 'BIL')
#context.stocks = symbols('DDM', 'MVV', 'QLD', 'SSO', 'UWM', 'SAA', 'UYM', 'UGE', 'UCC', 'UYG', 'RXL', 'UXI', 'DIG', 'URE', 'ROM', 'UPW', 'BIL')

schedule_function(rebalance,
                  date_rule=date_rules.month_start(),
                  time_rule=time_rules.market_open())


def rebalance(context, data):
  #Create stock dictionary of momentum
  MomList = GenerateMomentumList(context, data)

#sell all positions
for stock in context.portfolio.positions:
  order_target(stock, 0)
#create % weight
spy = symbol('SPY')
#if data[spy].price < data[spy].mavg(200):
#    order_target_percent(symbol('IEF'), 1)
#    return

weight = 0.95/context.topMom

#buy
for l in MomList:
  stock = l[0]
if stock in data and data[stock].close_price > data[stock].mavg(200):
  order_percent(stock, weight)
pass


def GenerateMomentumList(context, data):
  
  MomList = []
price_history = history(bar_count=context.lookback, frequency="1d", field='price')

for stock in context.stocks:
  now = price_history[stock].ix[-1]
old = price_history[stock].ix[0]
pct_change = (now - old) / old
#if now > data[stock].mavg(200):
MomList.append([stock, pct_change, price_history[stock].ix[0]])


#sort in descending order, the price change (%)

MomList = sorted(MomList, key=itemgetter(1), reverse=True)
#return only the top "topMom" number of securities
MomList = MomList[0:context.topMom]
print (MomList[0][0].symbol)

return MomList


def change(one, two):
  return(( two - one)/one)

def handle_data(context, data):
  pass