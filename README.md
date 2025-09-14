# FETCH-TWS-PRICE

A simple Python bot that connects to **Interactive Brokers Trader Workstation (TWS)** using the [ib_insync](https://github.com/erdewit/ib_insync) library, and fetches stock/forex/futures prices.

This project is meant as a **starter template** to set up your first TWS API bot.

---

## ⚡ Features
- Connects to Interactive Brokers’ TWS or IB Gateway.
- Requests live or delayed market data for contracts (Stocks, Forex, Futures, Indexes, etc.).
- Prints Bid/Ask/Last quotes directly to the terminal.
- Easy starting point to extend into full trading bots later.

---

## 📦 Requirements
- Interactive Brokers account (Paper Trading or Live).
- IBKR **TWS** or **IB Gateway** running locally.
- Python 3.9+  
- [`ib_insync`](https://pypi.org/project/ib-insync/)

Install requirements:

```bash
pip install ib-insync
```


## 🔌 Setup

1. Launch TWS or IB Gateway and log in (Paper mode recommended).
2 .In TWS:
   Go to File → Global Configuration → API → Settings
   Tick "Enable ActiveX and Socket Clients"
   Ensure port = 7497 (default for Paper mode; Live sometimes = 7496)
    Optional: add 127.0.0.1 to the Trusted IPs list
3. Clone this repo and open it in your editor.
