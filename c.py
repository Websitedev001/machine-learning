import pandas as pd
import matplotlib.pyplot as plt

# Load the data
stock_data = pd.read_stata("1.dta") 

# Define the SIC codes for the two industries of interest
industry1_sic = 5712
industry2_sic = 3663

# Filter the dataset to include only stocks from the selected industries
industry1_stocks = stock_data[stock_data['sic'] == industry1_sic]
industry2_stocks = stock_data[stock_data['sic'] == industry2_sic]

# Calculate monthly market cap for each industry
industry1_monthly_market_cap = industry1_stocks.groupby(['year', 'month'])['market_cap'].sum()
industry2_monthly_market_cap = industry2_stocks.groupby(['year', 'month'])['market_cap'].sum()

# Calculate monthly returns of the value-weighted portfolios
industry1_monthly_returns = industry1_stocks.groupby(['year', 'month']).apply(
    lambda x: (x['ret'] * (x['market_cap'] / industry1_monthly_market_cap.loc[(x.name[0], x.name[1])])).sum()
)
industry2_monthly_returns = industry2_stocks.groupby(['year', 'month']).apply(
    lambda x: (x['ret'] * (x['market_cap'] / industry2_monthly_market_cap.loc[(x.name[0], x.name[1])])).sum()
)

# Plot the monthly returns of the two portfolios
plt.plot(industry1_monthly_returns.index, industry1_monthly_returns.values, label='Industry 1', color='blue')
plt.plot(industry2_monthly_returns.index, industry2_monthly_returns.values, label='Industry 2', color='red')
plt.xlabel('Year-Month')
plt.ylabel('Monthly Returns')
plt.title('Value-Weighted Portfolio Monthly Returns')
plt.legend()
plt.show()
