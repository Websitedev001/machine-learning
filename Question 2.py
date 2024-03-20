import pandas as pd

# Load the data
prank1 = pd.read_stata("stock return processed.dta")

prank1c = prank1[['gvkey', 'datadate', 'ret', 'sp500_ret_m', 'Year', 'Month', 'Date']]

# The 90th percentile
top1 = prank1c[['sp500_ret_m', 'Year', 'Month']].groupby(['Year', 'Month'], as_index=False).quantile(0.9)
top1.rename(columns={'sp500_ret_m': 'sp500_ret_m_top'}, inplace=True)

# The 10th percentile
bot1 = prank1c[['sp500_ret_m', 'Year', 'Month']].groupby(['Year', 'Month'], as_index=False).quantile(0.1)
bot1.rename(columns={'sp500_ret_m': 'sp500_ret_m_bot'}, inplace=True)

# Merge top and bottom percentiles
prank2 = pd.merge(prank1c, top1, left_on=['Year', 'Month'], right_on=['Year', 'Month'], how='inner')
prank3 = pd.merge(prank2, bot1, left_on=['Year', 'Month'], right_on=['Year', 'Month'], how='inner')

# Find firms with the top 10% and bottom 10%
prank_top1 = prank3[prank3['sp500_ret_m'] >= prank3['sp500_ret_m_top']]
prank_bot1 = prank3[prank3['sp500_ret_m'] <= prank3['sp500_ret_m_bot']]

# Construct the equal-weighted portfolios for top and bottom
prank_top2 = prank_top1[['Year', 'Month', 'ret']].groupby(['Year', 'Month'], as_index=False).mean()
prank_top2.rename(columns={'ret': 'ret_top'}, inplace=True)
prank_top2['date'] = pd.to_datetime({'year': prank_top2['Year'], 'month': prank_top2['Month'], 'day': 28})

prank_bot2 = prank_bot1[['Year', 'Month', 'ret']].groupby(['Year', 'Month'], as_index=False).mean()
prank_bot2.rename(columns={'ret': 'ret_bot'}, inplace=True)
prank_bot2['date'] = pd.to_datetime({'year': prank_bot2['Year'], 'month': prank_bot2['Month'], 'day': 28})

# Display the resulting DataFrames
print("Top Portfolio:")
print(prank_top2)

print("\nBottom Portfolio:")
print(prank_bot2)


#Index(['sp500_ret_m', 'nasdaq_ret_m', 'r2000_ret_m', 'Year', 'Month', 'Date'], dtype='object')