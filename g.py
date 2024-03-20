import pandas as pd
import numpy as np

# Read the risk-free rate data from the Excel file
rf1 = pd.read_excel("D:/Investment Management and Machine Learning/Week 3/treasury bill.xls")

# Calculate the risk-free rate
rf1['rf'] = rf1['DGS3MO'] / 1200

# Group the risk-free rate data by year and month
rf2 = rf1.groupby(['Year', 'Month'], as_index=False)['rf'].mean()

# Merge the risk-free rate data with the portfolio data for the top portfolio
prank_top3 = pd.merge(prank_top2, rf2, on=['Year', 'Month'], how='inner')

# Calculate the excess returns for the top portfolio
prank_top3['ret_top_rf'] = prank_top3['ret_top'] - prank_top3['rf']

# Calculate the Sharpe Ratio for the top portfolio
SR_top = (prank_top3['ret_top_rf'].mean() * 12) / (prank_top3['ret_top_rf'].std() * np.sqrt(12))

# Merge the risk-free rate data with the portfolio data for the bottom portfolio
prank_bot3 = pd.merge(prank_bot2, rf2, on=['Year', 'Month'], how='inner')

# Calculate the excess returns for the bottom portfolio
prank_bot3['ret_bot_rf'] = prank_bot3['ret_bot'] - prank_bot3['rf']

# Calculate the Sharpe Ratio for the bottom portfolio
SR_bot = (prank_bot3['ret_bot_rf'].mean() * 12) / (prank_bot3['ret_bot_rf'].std() * np.sqrt(12))

# Report the Sharpe Ratios
print("Sharpe Ratio for the top portfolio:", SR_top)
print("Sharpe Ratio for the bottom portfolio:", SR_bot)
