from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

print("Connected:", ib.isConnected())

# Request delayed market data
ib.reqMarketDataType(3)   # <--- CRUCIAL line
# 1 = live
# 2 = frozen
# 3 = delayed
# 4 = delayed frozen

# Define the contract (Apple)
contract = Stock('AAPL', 'SMART', 'USD')

# Request ticker
market_data = ib.reqMktData(contract)

ib.sleep(2)  # Give IB time to respond

print("Ticker:", contract.symbol)
print("Last Price (delayed):", market_data.last)
print("Bid (delayed):", market_data.bid)
print("Ask (delayed):", market_data.ask)

ib.disconnect()