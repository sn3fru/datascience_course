#Import Logictic Regression model
from sklearn.linear_model import LogisticRegression

#Create a svm Classifier
clf = LogisticRegression()

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)