import pandas as pd

# Read the Stata data file
data = pd.read_stata('1.dta')

# Check the SIC value for a specific row (e.g., row 50)
sic_value = data.loc[1250, 'sic']
print("SIC value at row 50:", sic_value)
