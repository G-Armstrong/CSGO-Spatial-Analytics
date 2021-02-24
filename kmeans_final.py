import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#import sklearn.cluster.hierarchical as hclust
from sklearn import preprocessing
import seaborn as sns

#get player_df from csv
df = pd.read_csv('players_df.csv')

#drop array column [12]

#Do we need to normalize?
scaler = preprocessing.MinMaxScaler()
features_normal = scaler.fit_transform(df)
print(pd.DataFrame(features_normal).describe())

# #clustering
# kmeans = KMeans(n_clusters=4).fit(features_normal)
# labels = pd.DataFrame(kmeans.labels_) #This is where the label output of the KMeans we just ran lives. Make it a dataframe so we can concatenate back to the original data
# labeledColleges = pd.concat((features,labels),axis=1)
# labeledColleges = labeledColleges.rename({0:'labels'},axis=1)
# labeledColleges.head()

# #visualization
# sns.lmplot(x='Top10perc',y='S.F.Ratio',data=labeledColleges,hue='labels',fit_reg=False)
# sns.pairplot(labeledColleges,hue='labels')