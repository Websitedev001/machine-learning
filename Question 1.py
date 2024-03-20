# Import necessary libraries
import pandas as pd

# Load the data
prank1 = pd.read_stata("Inden return-1.dta")

# Create the variable for ranking
prank1['var_rank'] = prank1['sp500_ret_m']
prank1.dropna(subset=['var_rank'], inplace=True)

# Select necessary columns for further analysis
prank1a = prank1[['gvkey', 'datadate', 'ret', 'var_rank']]

# Display the resulting DataFrame
print(prank1.columns)


