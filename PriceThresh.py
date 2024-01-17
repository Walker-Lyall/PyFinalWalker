import tkinter as tk
from tkinter import ttk
import yfinance as yf

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        price = info.get("lastClose", "N/A")
        return price
    except Exception as e:
        return f"Error: {str(e)}"


def show_stocks():
    selected_price = float(price_threshold_entry.get())
    stocks_listbox.delete(0, tk.END)

    for stock_symbol in stock_symbols:
        stock_price = get_stock_data(stock_symbol)
        if stock_price != "N/A" and stock_price > selected_price:
            stocks_listbox.insert(tk.END, f"{stock_symbol}: ${stock_price}")


# Main GUI window
root = tk.Tk()
root.title("Stocks Over $100")

# Label and entry for price threshold
price_threshold_label = ttk.Label(root, text="Price Threshold:")
price_threshold_label.grid(row=0, column=0, padx=10, pady=10)
price_threshold_entry = ttk.Entry(root)
price_threshold_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to show stocks
show_stocks_button = ttk.Button(root, text="Show Stocks", command=show_stocks)
show_stocks_button.grid(row=0, column=2, padx=10, pady=10)

# Listbox to display stocks
stocks_listbox = tk.Listbox(root, width=40, height=10)
stocks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Sample stock symbols
stock_symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

# Run the GUI
root.mainloop()
