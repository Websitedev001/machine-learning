import pandas as pd
import matplotlib.pyplot as plt

# using the stock return processed.dta dataset
stock_data = pd.read_stata("1.dta")

# the SIC codes for the two industries of interest
industry1_sic = 5712 
industry2_sic = 3663  

# Filtering the dataset to include only the stocks from the selected industries
industry1_stocks = stock_data[stock_data['sic'] == industry1_sic]
industry2_stocks = stock_data[stock_data['sic'] == industry2_sic]

# Calculate monthly returns for each industry
industry1_returns = industry1_stocks.groupby(['datadate'])['ret'].mean()
industry2_returns = industry2_stocks.groupby(['datadate'])['ret'].mean()

# Calculate equal-weighted portfolio returns for each industry
industry1_portfolio_return = industry1_returns.groupby(pd.Grouper(freq='M')).mean()
industry2_portfolio_return = industry2_returns.groupby(pd.Grouper(freq='M')).mean()

# Plot the monthly returns of the two portfolios
plt.plot(industry1_portfolio_return.index, industry1_portfolio_return, label='Industry 1 Portfolio', color='blue')
plt.plot(industry2_portfolio_return.index, industry2_portfolio_return, label='Industry 2 Portfolio', color='red')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Monthly Return')
plt.title('Monthly Returns of Equal-Weighted Portfolios')
plt.legend()

# Display the plot
plt.show()
