import tkinter as tk
from tkinter import ttk

def apply_filters(): # once the button is pressed the scan through all the data 
    selected_filters = [filter_var.get() for filter_var in filter_vars]
    print("Selected Filters:", selected_filters)
    #search for stocks with the clicked filters bing tru, and unclicked being false

# Create the main window
root = tk.Tk()
root.title("Filter Checklist")

# Create a list of filters
filters = ["Over $5b Market Cap", "Over 500k Volume", "Dividend Yield > 5%", "Price > $100"]

# Create variables to store the state of each filter
filter_vars = [tk.BooleanVar() for _ in filters]

# Create checkboxes for each filter
for i, filter_text in enumerate(filters):
    checkbox = ttk.Checkbutton(root, text=filter_text, variable=filter_vars[i])
    checkbox.grid(row=i, column=0, sticky=tk.W)

# Create a button to apply filters
apply_button = ttk.Button(root, text="Apply Filters", command=apply_filters)
apply_button.grid(row=len(filters), column=0, pady=10)

#basically I have to apply these filter values onto values of stocks
# so if price over 100 is true, then the only show the stocks that share that same true value
# selected filters[3] must = stock[3]

# Run the Tkinter event loop
root.mainloop()
