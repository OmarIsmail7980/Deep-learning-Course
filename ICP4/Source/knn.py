import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('train.csv')

df.head()

df['sex'] = df.Sex.map({'male':1, 'female':0}).astype(int)

import matplotlib.pyplot as plt
import seaborn as sns

car = df.corr()


