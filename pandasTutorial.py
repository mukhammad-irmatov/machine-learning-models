import pandas as pd

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mean()
new_df = df.fillna(x)
print(new_df.to_string())
print(new_df.info())