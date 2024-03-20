import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# using the stock return processed.dta dataset
data = pd.read_stata('1.dta')

# Define the SIC codes for the two industries you want to select
sic_industry_1 = 5712
sic_industry_2 = 3663

# Filter the DataFrame to include only the rows corresponding to the desired SIC codes
industry_1_stocks = data[data['sic'] == sic_industry_1]
industry_2_stocks = data[data['sic'] == sic_industry_2]

# Calculate monthly returns for each stock
industry_1_stocks['monthly_return'] = industry_1_stocks.groupby('datadate')['ret'].transform('mean')
industry_2_stocks['monthly_return'] = industry_2_stocks.groupby('datadate')['ret'].transform('mean')

# Calculate equal-weighted portfolio returns for each month
portfolio_1_returns = industry_1_stocks.groupby('datadate')['monthly_return'].mean()
portfolio_2_returns = industry_2_stocks.groupby('datadate')['monthly_return'].mean()

# Plot the monthly returns of the two portfolios
plt.figure(figsize=(10, 6))
plt.plot(portfolio_1_returns.index, portfolio_1_returns.values, label='Industry 1 Portfolio')
plt.plot(portfolio_2_returns.index, portfolio_2_returns.values, label='Industry 2 Portfolio')
plt.title('Monthly Returns of Equal-Weighted Portfolios')
plt.xlabel('Date')
plt.ylabel('Monthly Return')
plt.legend()
plt.show()
