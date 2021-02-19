from sklearn.naive_bayes import GaussianNB
import pandas as pd

df = pd.read_csv("glass.csv")

print(df.isnull().sum()) 

#check correlation against target
for i in df.columns:
    print(df[[i,'Type']].corr(),'\n')

#drop low correlated features
df = df.drop('Ca',axis=1)
df = df.drop('K', axis=1)

X = df.copy()
X = X.drop('Type', axis=1)
y = df['Type']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

nb = GaussianNB()
nb.fit(x_train,y_train)
print(nb.score(x_test,y_test))
pred = nb.predict(x_test)



from sklearn.metrics import classification_report
print(classification_report(y_test,pred))

#only include highest corrleted features(Na,Mg,Al,Ba)
data = df[['Mg','Al','Ba','Type']]

X2 = data.copy()
X2 = X2.drop('Type', axis=1)
y2 = data['Type']

x_train2,x_test2,y_train2,y_test2 = train_test_split(X2,y2,test_size=0.2,random_state=1)
nb.fit(x_train2,y_train2)
pred2 = nb.predict(x_test2)
print(nb.score(x_test2,y_test2))
print(classification_report(y_test2,pred2))


