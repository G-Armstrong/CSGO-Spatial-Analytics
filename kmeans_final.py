import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#import sklearn.cluster.hierarchical as hclust
from sklearn import preprocessing
import seaborn as sns

#get player_df from csv
df = pd.read_csv('players_df.csv')

#remove columns we don't want to be factoring into kmeans
# features = df.drop(['time of kills', 'ID', 'Health'],axis=1)
features = df.drop('ID',axis=1)

#Do we need to normalize?
scaler = preprocessing.MinMaxScaler()
features_normal = scaler.fit_transform(features)

# normalized_pd = pd.DataFrame(features_normal)
# print(normalized_pd)

#Clustering
kmeans = KMeans(n_clusters=5).fit(features_normal)
#This is where the label output of the KMeans we just ran lives. 
#Make it a dataframe so we can concatenate back to the original data
print(pd.DataFrame(kmeans.labels_))
labels = pd.DataFrame(kmeans.labels_) 
labeledRoles = pd.concat((features,labels),axis=1)
labeledRoles = labeledRoles.rename({0:'labels'},axis=1)

#visualization
sns.lmplot(x='total kills',y='total deaths',data=labeledRoles,hue='labels',fit_reg=False)
#sns.pairplot(labeledRoles,hue='labels')







