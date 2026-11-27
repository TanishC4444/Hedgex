import yfinance as yf
# Create Ticker object
ticker = yf.Ticker("AAPL")

# Fetch basic company info
info = ticker.info
print("Company Info:")
print(info)

# Fetch historical market data
hist = ticker.history(period="5d")
print("\nLast 5 days of price data:")
print(hist)
