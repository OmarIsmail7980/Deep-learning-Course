import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.decomposition import PCA

raw_df = pd.read_csv('CC.csv')
#check the null values of each feature
print(raw_df.isnull().sum())


#fill all the null values with the mean
raw_df.fillna(value=raw_df['MINIMUM_PAYMENTS'].mean(), inplace=True)
#cehck for null values
print(raw_df.isnull().sum())
raw_df = raw_df.drop('CUST_ID', axis =1)

df = raw_df.copy()
x = df.copy()
x = x.drop('TENURE', axis=1)
y = df['TENURE']



wcss = []

for i in range(1,11):
     kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
     kmeans.fit(df)
     wcss.append(kmeans.inertia_)

y3 = np.array([1,2,3,4,5,6,7,8,9,10])
plt.plot(y3,wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

#store list 
k = wcss

kmeans=KMeans(n_clusters=2)
kmeans.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = kmeans.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)



#2
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


kmean2=KMeans(n_clusters=2)
kmean2.fit(x)

# predict the cluster for each data point
y_cluster2 = kmean2.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster2)
print(score)


#3)
# Apply transform to the data
pca = PCA(2)
x_pca = pca.fit_transform(X_scaled)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,df[['TENURE']]],axis=1)
print(finaldf)

kmean3=KMeans(n_clusters=2)
kmean3.fit(finaldf)

# predict the cluster for each data point
y_cluster3 = kmean3.predict(finaldf)
from sklearn import metrics
score3 = metrics.silhouette_score(X_scaled, y_cluster3)
print(score3)










