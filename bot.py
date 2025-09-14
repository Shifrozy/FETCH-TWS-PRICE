from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

fx = Forex('EURUSD')
ticker = ib.reqMktData(fx)

for _ in range(5):  # check a few times
    ib.sleep(2)
    print("EUR/USD -> Bid:", ticker.bid, " Ask:", ticker.ask, " Last:", ticker.last)

ib.disconnect()