import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the dataset using read_csv
df = pd.read_csv("stock.csv",
                 parse_dates=True,
                 index_col="Date")




# deleting column
df.drop(columns='Unnamed: 0')

df.plot(subplots=True, figsize=(10, 12))