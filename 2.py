import pandas as pd

# Read the Stata data file into a DataFrame
data = pd.read_stata('1.dta')

# Define the two SIC codes you want to filter for
sic_codes = [5712, 3663]  # Replace with your desired SIC codes

# Filter the data based on the SIC codes
filtered_data = data[data['sic'].isin(sic_codes)]

# Display the filtered data
print(filtered_data)
