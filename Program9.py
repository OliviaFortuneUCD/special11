#Ranking
import pandas as pd
import seaborn as sns

# reading the dataset using read_csv
data = pd.read_csv('Rankings.csv', encoding = "cp1252")
print(data.head)
# creating a rank column and passing the returned rank series
data["Rank"] = data["Rank"].rank()
# sorting w.r.t name column
#data.sort_values("Country", inplace = True)
#df1=data.sort_values(by=['Rank']).head(5)
df2= data[data["Country"] == 'Ireland']
df3=df2.sort_values(by=['Rank']).head(5)

p = sns.regplot(x="Score", y="University", data=df3, color = "blue")