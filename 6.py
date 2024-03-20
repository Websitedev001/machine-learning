import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# Set plot size will create a new figure with a width of 25 inches and a height of 15 inches.
plt.figure(figsize=(25, 15))

# Read the Stata file
data = pd.read_stata('1.dta')

# Display the first few rows of the dataframe
print(data.head())