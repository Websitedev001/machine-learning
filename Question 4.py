"""import pandas as pd

# Load the data
prank1 = pd.read_stata("1.dta")
# For ranking
prank1['var_rank'] = prank1['dlttq'] / prank1['atq']
prank1.dropna(subset=['var_rank'], inplace=True)

# Select necessary columns for further analysis
prank1a = prank1[['gvkey', 'datadate', 'ret', 'var_rank']]

# Printing results
print(prank1a)


#variables at 1.dta are 
#Index(['sp500_ret_m', 'nasdaq_ret_m', 'r2000_ret_m', 'Year', 'Month', 'Date'], dtype='object')"""


import statsmodels.api as sm

Factor = pd.read_excel("factors.xlsx")

# Merge factors with portfolio returns data
prank_top_factor1 = pd.merge(prank_top2, Factor, on=['Year', 'Month'], how='inner')
prank_bot_factor1 = pd.merge(prank_bot2, Factor, on=['Year', 'Month'], how='inner')

# Calculate excess returns over risk-free rate
prank_top_factor1['ret_top_rf'] = prank_top_factor1['ret_top'] - prank_top_factor1['RF']
prank_bot_factor1['ret_bot_rf'] = prank_bot_factor1['ret_bot'] - prank_bot_factor1['RF']

# Add constant for regression
prank_top_factor1 = sm.add_constant(prank_top_factor1)
prank_bot_factor1 = sm.add_constant(prank_bot_factor1)

# Regression analysis
# Top Portfolio
reg_top_factor = sm.OLS(prank_top_factor1['ret_top_rf'], 
                        prank_top_factor1[['const', 'MktRF', 'SMB', 'HML', 'MOM', 'RMW', 'CMA']]
                       ).fit().get_robustcov_results(cov_type='HC0')
print(reg_top_factor.summary())

# Bottom Portfolio
reg_bot_factor = sm.OLS(prank_bot_factor1['ret_bot_rf'], 
                        prank_bot_factor1[['const', 'MktRF', 'SMB', 'HML', 'MOM', 'RMW', 'CMA']]
                       ).fit().get_robustcov_results(cov_type='HC0')
print(reg_bot_factor.summary())
