import pandas as pd
#df = pd.read_csv("weather.csv")
#df.to_csv("weather.dat", sep = " ")

df = pd.read_csv("weather.dat", sep=" ")

df['spread'] = df['max_temp'] - df['min_temp']
print (df)

max_spread = df[["year","spread"]].max()
print(max_spread)
