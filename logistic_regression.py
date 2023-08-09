# Split values
x = df.iloc[:, 0: -1]
y = df.iloc[:, -1]

x_train,x_test,y_train,y_test=train_test_split(X,trainy,test_size=0.20,random_state=42)


from sklearn.linear_model import LogisticRegression

lg=LogisticRegression()
lg.fit(x_train,y_train)
print("Model score: ",lg.score(x_train,y_train))
lgpred=lg.predict(x_test)
print("Accuracy Score: ",accuracy_score(y_test,lgpred))
print("Confusion Matrix: ",confusion_matrix(y_test,lgpred))
print("Classification report: ",classification_report(y_test,lgpred))
