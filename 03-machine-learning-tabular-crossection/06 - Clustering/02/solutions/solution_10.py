
from sklearn.cluster import DBSCAN

dbsc = DBSCAN(eps = .5, min_samples = 15).fit(df)