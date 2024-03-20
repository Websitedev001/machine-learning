import pandas as pd

# Read the processed data file into a DataFrame
data = pd.read_stata('1.dta')

# Define the SIC codes for the two industries you want to select
sic_industry_1 = 5712
sic_industry_2 = 3663

# Filter the DataFrame to include only the rows corresponding to the desired SIC codes
industry_1_stocks = data[data['sic'] == sic_industry_1]
industry_2_stocks = data[data['sic'] == sic_industry_2]

# Display the selected stocks for each industry
print("Stocks in Industry 1 (SIC {}):".format(sic_industry_1))
print(industry_1_stocks)

print("\nStocks in Industry 2 (SIC {}):".format(sic_industry_2))
print(industry_2_stocks)
