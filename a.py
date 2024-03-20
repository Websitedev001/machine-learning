import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# using the stock return processed.dta dataset
stock_data = pd.read_stata("1.dta")

# the SIC codes for the two industries of interest
industry1_sic = 5712 
industry2_sic = 3663  

# Filtering the dataset to include only the stocks from the selected industries which hace sic of 5712 and 3663
industry1_stocks = stock_data[stock_data['sic'] == industry1_sic]
industry2_stocks = stock_data[stock_data['sic'] == industry2_sic]

# Print the filtered datasets
print("Stocks in Industry 1 (SIC Code {}):\n".format(industry1_sic), industry1_stocks)
print("\nStocks in Industry 2 (SIC Code {}):\n".format(industry2_sic), industry2_stocks)
