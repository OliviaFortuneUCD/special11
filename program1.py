#Timeseries
# Import Library

import matplotlib.pyplot as plt
import pandas as pd

# Defne Data

timeseries_data = {
    'Date': ['2021-12-26', '2021-12-29',
             '2021-12-27', '2021-12-30',
             '2021-12-28', '2021-12-31'],

    'Washington': [42, 41, 41, 42, 42, 40],

    'Canada': [30, 30, 31, 30, 30, 30],

    'California': [51, 50, 50, 50, 50, 50]
}

# Create dataframe

dataframe = pd.DataFrame(timeseries_data, columns=['Date', 'Washington', 'Canada', 'California'])

# Changing the datatype

dataframe["Date"] = dataframe["Date"].astype("datetime64")

# Setting the Date as index

dataframe = dataframe.set_index("Date")

# Import Library



# Plot

plt.plot(dataframe["Canada"], marker='o')

# Labelling

plt.xlabel("Date")
plt.ylabel("Temp in Faherenheit")
plt.title("Pandas Time Series Plot")

# Display

plt.show()
