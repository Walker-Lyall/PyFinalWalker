import tkinter as tk
from tkinter import ttk
import yfinance as yf

def filter_stocks():
    symbol = symbol_entry.get()
    criteria = criteria_entry.get()
    
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d')
        
        if not data.empty:
            result_text.set(f"Stock Symbol: {symbol}\n\nCriteria: {criteria}\n\nStock Data:\n{data}")
        else:
            result_text.set("Error: Unable to fetch stock data.")
    except Exception as e:
        result_text.set(f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Stock Screener")

# Create and pack widgets
symbol_label = tk.Label(root, text="Enter Stock Symbol:")
symbol_label.pack(pady=10)

symbol_entry = tk.Entry(root, width=10)
symbol_entry.pack(pady=10)

criteria_label = tk.Label(root, text="Enter Screening Criteria:")
criteria_label.pack(pady=10)

criteria_entry = tk.Entry(root, width=10)
criteria_entry.pack(pady=10)

filter_button = tk.Button(root, text="Filter Stocks", command=filter_stocks)
filter_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()

