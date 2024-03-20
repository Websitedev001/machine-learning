import pandas as pd

# Replace 'your_file.dta' with the path to your Stata data file
data = pd.read_stata('Stock Return.dta')

# Select the first 100 records
data_first_100 = data.head(100)

# Display the first few rows of the dataframe
print(data_first_100)


