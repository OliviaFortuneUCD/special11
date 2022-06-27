#Ranking
import pandas as pd

#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
                   'points': [10, 10, 12, 15, 19, 23, 20, 20, 26]})

#view DataFrame
print(df)

#add ranking column to data frame
df['points_rank'] = df.groupby(['team'])['points'].rank()

#view updated DataFrame
print(df)