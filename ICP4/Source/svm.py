import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier


train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
X_train = train_df.drop("Survived",axis=1)
Y_train = train_df["Survived"]
X_test = test_df.drop("PassengerId",axis=1).copy()
print(train_df[train_df.isnull().any(axis=1)])

##SVM
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)

#correlation between Sex and Survived
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(train_df['Sex'],hue=train_df['Survived'])

#correlation between Sex and Survived
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(train_df['Sex'],hue=train_df['Survived'])
#From the plot it looks one gender had way more survivors than the other.

#let's check the correlation
print(train_df[['Sex','Survived']].corr())# there a strong correlation between the features and we should keep it