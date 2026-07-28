import yfinance as yf
import matplotlib.pyplot as plt

# Step 1: Request user input for any stock or crypto ticker
user_choice = input("Enter ticker symbol (e.g., NVDA, AAPL, TSLA, BTC-USD): ")
print(f"\n[INFO]: Fetching fresh data for {user_choice}...")

# Step 2: Download data from Yahoo Finance for the last 3 months
data = yf.download(user_choice, period="3mo")

# Step 3: Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], color="orange", linewidth=2)

# Step 4: Format the chart labels and grid
plt.title(f"Interactive Chart for {user_choice}")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.grid(True)

# Step 5: Render the final plot
plt.show()
print(f"[SUCCESS]: Dynamic analysis for {user_choice} completed successfully!")
