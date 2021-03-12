#Question 3
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation

data = pd.read_csv("breas Cancer.csv")
#check for null values
print(data.isnull().sum())

#drop unnecassary variables
data  = data.drop(['Unnamed: 32','id'], axis = 1)
#check the number of classes
print(data['diagnosis'].value_counts())
#encode classes
data['diagnosis'] = data['diagnosis'].map({'B':1, 'M':0})

#split data
X = data.copy()
X = X.drop('diagnosis',axis=1)
y = data['diagnosis']

#Standardize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=0)

model = Sequential()
#hidden layers
model.add(Dense(20,input_dim = 30,activation = 'relu' ))
model.add(Dense(20,activation='relu')) 
model.add(Dense(20,activation = 'relu')) 
#output layer 
model.add(Dense(1,activation='sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer='Adam', metrics = ['acc']) 
#train model
model.fit(x_train,y_train,verbose=1,epochs=100)

print(model.summary())
print(model.evaluate(x_test,y_test))
          