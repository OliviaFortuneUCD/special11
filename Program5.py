# Initialising required libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# ABC colllege classes by date- from 01-11-2021 to 07-11-2021
abc = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i + 1)
                                              for i in range(7)]),
                    'classes': [5, 6, 8, 2, 3, 7, 4]})

# XYZ colllege classes by date - from 01-11-2021 to 07-11-2021
xyz = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i + 1)
                                              for i in range(7)]),
                    'classes': [2, 3, 7, 3, 4, 1, 2]})

# plotting the time series of ABC college dataframe
plt.plot(abc.date_of_week, abc.classes)

# plotting the time series of XYZ college dataframe
plt.plot(xyz.date_of_week, xyz.classes, color='green')

# Giving title to the graph
plt.title('Classes by Date')

# rotating the x-axis tick labels at 30degree
# towards right
plt.xticks(rotation=30, ha='right')

# Giving x and y label to the graph
plt.xlabel('Date')
plt.ylabel('Classes')