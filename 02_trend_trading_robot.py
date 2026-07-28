import yfinance as yf

# Step 1: Download Bitcoin data for the last 6 months
data = yf.download("BTC-USD", period="6mo")

# Step 2: Clean the data structure using squeeze
close_prices = data['Close'].squeeze()

# Step 3: Calculate the 10-day Moving Average (Trend Line)
ma10 = close_prices.rolling(window=10).mean()

print("🤖 [SYSTEM]: Starting Bitcoin market scan...")
print("-" * 50)

# Step 4: Loop through the history to detect trend changes (Longs)
for i in range(10, len(close_prices)):
    yesterday_price = float(close_prices.iloc[i-1])
    yesterday_ma = float(ma10.iloc[i-1])
    
    today_price = float(close_prices.iloc[i])
    today_ma = float(ma10.iloc[i])
    
    # Logic condition: Price crosses Moving Average from bottom to top
    if (yesterday_price < yesterday_ma) and (today_price > today_ma):
        signal_date = data.index[i].strftime('%Y-%m-%d')
        btc_price = int(today_price)
        print(f"🟢 BUY SIGNAL DETECTED: {signal_date} -> Entry Price: ${btc_price}")

print("-" * 50)
print("🤖 [SYSTEM]: Market scan successfully finished!")
