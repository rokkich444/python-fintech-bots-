import yfinance as yf
import matplotlib.pyplot as plt

# Step 1: Download Bitcoin historical data
print("[INFO]: Gathering data for automated report generation...")
data = yf.download("BTC-USD", period="3mo")

# Step 2: Build and design the analytical chart
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], color="orange", linewidth=2)

plt.title("Automated Financial Report: Bitcoin (BTC-USD)")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.grid(True)

# Step 3: Save the figure directly to a file before showing it
# This file can be uploaded straight to your GitHub repository
output_filename = 'btc_report_2026.png'
plt.savefig(output_filename, dpi=300)

# Step 4: Show the output on screen
plt.show()
print(f"🤖 [SYSTEM]: Analytics report image successfully saved as '{output_filename}'!")
