#question b
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

# Read the data
port1 = pd.read_stata("1.dta")

# Extract Year and Month from the datadate column
port1['Year'] = port1['datadate'].dt.year
port1['Month'] = port1['datadate'].dt.month

# Equally weight all stocks in the sample
ew1 = port1[['ret', 'Year', 'Month']]
ew1.dropna(inplace=True)
ew2 = ew1.groupby(['Year', 'Month'], as_index=False).mean()
ew2.rename(columns={'ret': 'ret_ew'}, inplace=True)
ew2['date'] = pd.to_datetime({'year': ew2['Year'], 'month': ew2['Month'], 'day': 28})

# Plot the equal-weighted portfolio return
plt.plot(ew2['date'], ew2['ret_ew'], color='green', linewidth=5)
plt.xlabel('Date', fontsize=20)
plt.ylabel('Return', fontsize=20)
plt.title('Equal-weighted Portfolio Return', fontsize=20)
plt.legend(['Equal-weighted Portfolio'], fontsize=20)
plt.gca().xaxis.set_major_locator(dates.YearLocator(3, month=12, day=31))
plt.show()

