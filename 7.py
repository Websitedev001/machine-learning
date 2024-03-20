import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the Stata file into a DataFrame
port = pd.read_stata('1.dta')

# Extract the year from the 'datadate' column
port['Year'] = port['datadate'].dt.year

# Drop missing values inplace
port.dropna(inplace=True)

# Set up the plot
plt.figure(figsize=(25, 15))

# Plotting
plt.ylabel('Return', fontsize=20)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=-1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Display the plot
plt.show()
