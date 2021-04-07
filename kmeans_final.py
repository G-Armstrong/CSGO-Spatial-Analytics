import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#import sklearn.cluster.hierarchical as hclust
from sklearn import preprocessing
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA

#Sources
#https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

kvalue = 5

#get player_df from csv
features = pd.read_csv('players_df.csv')
raw_data = make_blobs(n_samples = 2320, n_features = 22, centers = kvalue, cluster_std = 1)

#Do we need to normalize?
scaler = preprocessing.MinMaxScaler()
features_normal = scaler.fit_transform(features)

normalized_pd = pd.DataFrame(features_normal)


#Clustering
kmeans = KMeans(n_clusters=kvalue, n_init=100).fit(features_normal)
#This is where the label output of the KMeans we just ran lives. 
#Make it a dataframe so we can concatenate back to the original data
labels = pd.DataFrame(kmeans.labels_)
labeledRoles = pd.concat((features,labels),axis=1)
df_with_clusters = labeledRoles.rename({0:'clusters'},axis=1)
#print(kmeans.cluster_centers_)

#PCA Analysis 
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(features_normal)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

#append new columns
df_with_clusters['principal component 1']= principalDf['principal component 1']
df_with_clusters['principal component 2']= principalDf['principal component 2']

#vizualiztion
fig = plt.figure(figsize = (20,20))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = [0,1,2,3,4]
colors = ['red', 'green', 'blue', 'orange', 'purple']
for target, color in zip(targets,colors):
    indicesToKeep = df_with_clusters['clusters'] == target
    ax.scatter(df_with_clusters.loc[indicesToKeep, 'principal component 1']
               , df_with_clusters.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()



#visualization
plt.figure(figsize=(20,20))
#sns.lmplot(x='total kills',y='total deaths',data=labeledRoles,hue='labels',fit_reg=False)
#sns.pairplot(labeledRoles,hue='labels')
plt.scatter(raw_data[0][:,0], raw_data[0][:,1],c=kmeans.labels_)







