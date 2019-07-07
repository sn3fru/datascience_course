
from sklearn.preprocessing import MinMaxScaler
 
# Very important to scale!
sc = MinMaxScaler()
X = sc.fit_transform(X)