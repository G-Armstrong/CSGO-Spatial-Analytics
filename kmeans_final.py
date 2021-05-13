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

#create 5 random center points for pc1 and pc2
raw_data = make_blobs(n_samples = 2320, n_features = 2, centers = kvalue, cluster_std = 1)

#Normalize
scaler = preprocessing.MinMaxScaler()
features_normal = scaler.fit_transform(features)

normalized_pd = pd.DataFrame(features_normal)

#PCA Analysis 
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(features_normal)
principalDf = pd.DataFrame(data = principalComponents
              , columns = ['principal component 1', 'principal component 2'])

#Clustering
kmeans = KMeans(n_clusters=kvalue, n_init=100).fit(principalDf)

#This is where the label output of the KMeans we just ran lives. 
temp = pd.DataFrame(kmeans.labels_)
labels = kmeans.fit_predict(temp)

#add cluster column to pca df
labeledRoles = pd.concat((principalDf,temp),axis=1)


#print(kmeans.cluster_centers_)

#filter rows of original data
filtered_label0 = labeledRoles[labels == 0] 
filtered_label1 = labeledRoles[labels == 1]
filtered_label2 = labeledRoles[labels == 2]
filtered_label3 = labeledRoles[labels == 3]
filtered_label4 = labeledRoles[labels == 4]

#take pc1 as list
pc1_list0 = filtered_label0['principal component 1'].to_numpy()
pc1_list1 = filtered_label1['principal component 1'].to_numpy()

#take pc2 as list
pc2_list0 = filtered_label0['principal component 2'].to_numpy()
pc2_list1 = filtered_label1['principal component 2'].to_numpy()
 
#Plotting the results
plt.figure(figsize=(20,20))
plt.scatter(pc1_list0, pc2_list0 , color = 'red')
plt.scatter(pc1_list1, pc2_list1 , color = 'black')

plt.show()

#rename column 3 from "0" to "clusters"



# #vizualiztion
# fig = plt.figure(figsize = (20,20))
# ax = fig.add_subplot(1,1,1) 
# ax.set_xlabel('Principal Component 1', fontsize = 15)
# ax.set_ylabel('Principal Component 2', fontsize = 15)
# ax.set_title('2 component PCA', fontsize = 20)
# targets = [0,1,2,3,4]
# colors = ['red', 'green', 'blue', 'orange', 'purple']
# for target, color in zip(targets,colors):
#     indicesToKeep = labeledRoles['0'] == target
#     ax.scatter(labeledRoles.loc[indicesToKeep, 'principal component 1']
#                 , labeledRoles.loc[indicesToKeep, 'principal component 2']
#                 , c = color
#                 , s = 50)
# ax.legend(targets)
# ax.grid()



#visualization
plt.figure(figsize=(20,20))
#sns.lmplot(x='total kills',y='total deaths',data=labeledRoles,hue='labels',fit_reg=False)
#sns.pairplot(labeledRoles,hue='labels')
plt.scatter(raw_data[0][:,0], raw_data[0][:,1],c=kmeans.labels_)





























































# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
# from sklearn.cluster import KMeans
# #import sklearn.cluster.hierarchical as hclust
# from sklearn import preprocessing
# import seaborn as sns
# from sklearn.datasets import make_blobs
# from sklearn.decomposition import PCA

# #Sources
# #https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

# kvalue = 5

# #get player_df from csv
# features = pd.read_csv('players_df.csv')
# raw_data = make_blobs(n_samples = 2241, n_features = 39, centers = kvalue, cluster_std = 1)

# #Normalize
# scaler = preprocessing.MinMaxScaler()
# features_normal = scaler.fit_transform(features)

# normalized_pd = pd.DataFrame(features_normal)


# #Clustering
# kmeans = KMeans(n_clusters=kvalue, n_init=100).fit(features_normal)

# #This is where the label output of the KMeans we just ran lives. 
# labels = pd.DataFrame(kmeans.labels_)
# labeledRoles = pd.concat((normalized_pd,labels),axis=1)
# df_with_clusters = labeledRoles.rename({0:'clusters'},axis=1)
# #print(kmeans.cluster_centers_)

# #PCA Analysis 
# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(features_normal)
# principalDf = pd.DataFrame(data = principalComponents
#               , columns = ['principal component 1', 'principal component 2'])

# #append new columns
# df_with_clusters['principal component 1']= principalDf['principal component 1']
# df_with_clusters['principal component 2']= principalDf['principal component 2']

# #vizualiztion
# fig = plt.figure(figsize = (20,20))
# ax = fig.add_subplot(1,1,1) 
# ax.set_xlabel('Principal Component 1', fontsize = 15)
# ax.set_ylabel('Principal Component 2', fontsize = 15)
# ax.set_title('2 component PCA', fontsize = 20)
# targets = [0,1,2,3,4]
# colors = ['red', 'green', 'blue', 'orange', 'purple']
# for target, color in zip(targets,colors):
#     indicesToKeep = df_with_clusters['clusters'] == target
#     ax.scatter(df_with_clusters.loc[indicesToKeep, 'principal component 1']
#                 , df_with_clusters.loc[indicesToKeep, 'principal component 2']
#                 , c = color
#                 , s = 50)
# ax.legend(targets)
# ax.grid()



# #visualization
# plt.figure(figsize=(20,20))
# #sns.lmplot(x='total kills',y='total deaths',data=labeledRoles,hue='labels',fit_reg=False)
# #sns.pairplot(labeledRoles,hue='labels')
# plt.scatter(raw_data[0][:,0], raw_data[0][:,1],c=kmeans.labels_)






