
# Fitting Logistic Regression To the training set 
from sklearn.linear_model import LogisticRegression   
  
classifier = LogisticRegression(random_state = 42) 
classifier.fit(X_train, y_train) 