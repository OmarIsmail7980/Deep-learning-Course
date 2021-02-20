import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

plt.scatter(df['GarageArea'], df['SalePrice'])

#removing outlier using std and mean
mean = np.mean(df['GarageArea'])
std = np.std(df['GarageArea'])
upper2 = mean + 3*std
lower2 = mean - 3*std
            
df2 = df[(df['GarageArea']<upper2)& (df['GarageArea']>lower2)]


#removing outlier using Interquantile Range
q3=df['GarageArea'].quantile(.75)
q1=df['GarageArea'].quantile(.25)
iqr = q3-q1
upper = q3+1.5*iqr
lower = q1-1.5*iqr

df3 = df[(df['GarageArea']>lower) &(df['GarageArea']<upper)]


plt.scatter(df3['GarageArea'], df3['SalePrice'])








    