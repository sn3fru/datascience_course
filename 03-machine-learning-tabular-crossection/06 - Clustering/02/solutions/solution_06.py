from sklearn.cluster import MeanShift

ms = MeanShift()
ms.fit(X)
cluster_centers = ms.cluster_centers_