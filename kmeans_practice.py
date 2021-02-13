# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:31:40 2021

@author: rvanza632
"""


from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


X = np.array([[1, 2, 3, 6, 1], [1, 4, 5, 6, 5], [1, 0, 1, 6, 10],[10, 2, 9, 8, 15], [10, 4, 5, 11, 5], [10, 0, 9, 10, 50]])

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

#assigns points in X to a centroid number (0,1,2)
print(kmeans.labels_)
#given a point which cluster does it belong
print(kmeans.predict([[0, 0, 0, 0, 0], [12, 3, 5, 10, 50]]))


kmeans = kmeans.cluster_centers_

print(kmeans)
