# Import Library

import pandas as pd
import matplotlib.pyplot as plt

# Read csv

data= pd.read_csv('Sales.csv')

# Convert data frame

df=pd.DataFrame(data)

# Initilaize list

X = list(df.iloc[:,0])
Y = list(df.iloc[:,1])

# Set figure

plt.figure(figsize=(15, 5))

# Bar Plot

plt.bar(X, Y)

# Setting Ticks

plt.tick_params(axis='x',labelsize=15,rotation=90)
plt.tight_layout()

# Display

plt.show()