# Import Library

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read csv

data= pd.read_csv('Sales.csv')

# Convert to dataframe

df=pd.DataFrame(data)

# Initilaize list

X = list(df.iloc[:,0])
Y = list(df.iloc[:,1])

# Set figure

plt.figure(figsize=(5,5))

# Seaborn

sns.lineplot(x=X, y=Y)

# Setting Ticks

plt.tick_params(axis='x',labelsize=15,rotation=90)
plt.tight_layout()

# Display

plt.show()