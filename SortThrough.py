import yfinance as yf

def get_stock_data(symbol, start_date, end_date):
    # Download historical data for the given stock symbol and date range
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def filter_stocks(stock_data, min_price, max_price, min_volume):
    # Apply filters based on price and volume
    filtered_stocks = stock_data[
        (stock_data['Close'] >= min_price) &
        (stock_data['Close'] <= max_price) &
        (stock_data['Volume'] >= min_volume)
    ]
    return filtered_stocks

# Example usage:
symbol = 'AAPL'  # Example stock symbol (you can change it to any valid symbol)
start_date = '2022-01-01'  # Example start date
end_date = '2022-12-31'    # Example end date
min_price = 100  # Example minimum price filter
max_price = 200  # Example maximum price filter
min_volume = 1000000  # Example minimum volume filter

# Get stock data
stock_data = get_stock_data(symbol, start_date, end_date)

# Apply filters
filtered_stocks = filter_stocks(stock_data, min_price, max_price, min_volume)

# Display the filtered stocks
print(filtered_stocks)
