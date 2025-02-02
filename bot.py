import ccxt

exchange = ccxt.binance()
balance = exchange.fetch_balance()
print(f"Баланс: {balance['total']['USDT']} USDT")

ticker = "BTC/USDT"
price = exchange.fetch_ticker(ticker)['last']
print(f"Поточна ціна {ticker}: ${price}")

if price < 30000:
    print("💰 Купуємо BTC!")
    # exchange.create_market_buy_order(ticker, 0.01)
