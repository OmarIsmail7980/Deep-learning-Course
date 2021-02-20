import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

raw_data = pd.read_csv("ResturantRev.csv")
raw_data = raw_data.drop("Id", axis=1)
from sklearn.preprocessing import LabelEncoder
data = raw_data.copy()
data['City Group']= LabelEncoder().fit_transform(data['City Group'])
data['Type']= LabelEncoder().fit_transform(data['Type'])

y=data['revenue']
X = data.copy()
X = X.drop('revenue', axis = 1)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
reg = LinearRegression()
reg.fit(x_train,y_train)
pred = reg.predict(x_test)
print(mean_squared_error(y_test,pred))
print(reg.score(x_test,y_test))

#check correlation against target
for i in data.columns: 
    print(data[[i,'revenue']].corr(),'\n')

new_df = data[['City Group','P2','P6','P28','P29','revenue']]
y2=new_df['revenue']
X2 = new_df.copy()
X2= X2.drop('revenue', axis = 1)
x_train2,x_test2,y_train2,y_test2 = train_test_split(X2,y2,test_size=0.2,random_state=1)
reg = LinearRegression()
reg.fit(x_train2,y_train2)
pred2 = reg.predict(x_test2)

print(mean_squared_error(y_test2,pred))
print(reg.score(x_test2,y_test2))



