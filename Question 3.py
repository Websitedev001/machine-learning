import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#One independent variable
data1 = pd.read_excel("Linear Regression Example.xlsx", "Sheet1")
x = data1[['X']]
y = data1[['Y']]
x_cons = sm.add_constant(x)

# Regression Analysis for One Independent Variable
reg1 = sm.OLS(y, x_cons).fit().get_robustcov_results(cov_type='HC0')
#.get_robustcov_results(cov_type='HC0') helps correct minor errors in calculating p value
# coefficient on const is the intercept of the model

# Construct the equal-weighted portfolios for top and bottom percentiles
prank_top2 = prank_top1[['Year', 'Month', 'ret']].groupby(['Year', 'Month'], as_index=False).mean()
prank_top2.rename(columns={'ret': 'ret_top'}, inplace=True)
prank_top2['date'] = pd.to_datetime({'year': prank_top2['Year'], 'month': prank_top2['Month'], 'day': 28})

prank_bot2 = prank_bot1[['Year', 'Month', 'ret']].groupby(['Year', 'Month'], as_index=False).mean()
prank_bot2.rename(columns={'ret': 'ret_bot'}, inplace=True)
prank_bot2['date'] = pd.to_datetime({'year': prank_bot2['Year'], 'month': prank_bot2['Month'], 'day': 28})

# Average portfolio monthly return is positive. But the monthly returns distribute around zero
print(prank_top2['ret_top'].mean())

plt.hist(prank_top2['ret_top'], bins=100, range=(-0.5, 0.5), rwidth=0.8, color='green')

# Add the average portfolio return in excess of SP500 index returns
prank_top3 = pd.merge(prank_top2, indexret1, on=['Year', 'Month'], how='inner')
prank_top3['ret_top_ex'] = prank_top3['ret_top'] - prank_top3['sp500_ret_m']

prank_bot3 = pd.merge(prank_bot2, indexret1, on=['Year', 'Month'], how='inner')
prank_bot3['ret_bot_ex'] = prank_bot3['ret_bot'] - prank_bot3['sp500_ret_m']

# Regression Analysis
# Top Portfolio
prank_top3 = sm.add_constant(prank_top3)
reg_top = sm.OLS(prank_top3[['ret_top', 'ret_top_ex']], prank_top3[['const']]).fit().get_robustcov_results(cov_type='HC0')
print(reg_top.summary())

# Bottom Portfolio
prank_bot3 = sm.add_constant(prank_bot3)
reg_bot = sm.OLS(prank_bot3[['ret_bot', 'ret_bot_ex']], prank_bot3[['const']]).fit().get_robustcov_results(cov_type='HC0')
print(reg_bot.summary())
