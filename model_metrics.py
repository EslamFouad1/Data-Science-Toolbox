## Functions

# K-Fold Cross-Validation
# https://www.section.io/engineering-education/how-to-implement-k-fold-cross-validation/

from sklearn.model_selection import cross_validate

def cross_validation(model, _X, _y, _cv=5):
    _scoring = ['accuracy', 'precision', 'recall', 'f1']
    results = cross_validate(estimator=model,X=_X,y=_y,cv=_cv,scoring=_scoring,return_train_score=True)
    return {"Training Accuracy scores": results['train_accuracy'],
              "Mean Training Accuracy": results['train_accuracy'].mean()*100,
              "Training Precision scores": results['train_precision'],
              "Mean Training Precision": results['train_precision'].mean(),
              "Training Recall scores": results['train_recall'],
              "Mean Training Recall": results['train_recall'].mean(),
              "Training F1 scores": results['train_f1'],
              "Mean Training F1 Score": results['train_f1'].mean(),
              "Validation Accuracy scores": results['test_accuracy'],
              "Mean Validation Accuracy": results['test_accuracy'].mean()*100,
              "Validation Precision scores": results['test_precision'],
              "Mean Validation Precision": results['test_precision'].mean(),
              "Validation Recall scores": results['test_recall'],
              "Mean Validation Recall": results['test_recall'].mean(),
              "Validation F1 scores": results['test_f1'],
              "Mean Validation F1 Score": results['test_f1'].mean()
              }  

# Print confusion matrix heatmap
def print_confusion_matrix(y_true,y_pred):
    
    cf_matrix = confusion_matrix(y_true,y_pred)
    
    group_names = ["True Neg","False Pos","False Neg","True Pos"]
    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
    
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    
    plt.figure(figsize=(5, 5))
    sns.heatmap(cf_matrix, annot=labels, fmt="", cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def plot_auc_roc_curve(model,X_test,y_test):
    pred_prob = model.predict_proba(X_test)
    
    # roc curve and auc score for model
    fpr, tpr, thresh = roc_curve(y_test, pred_prob[:,1], pos_label=1)
    auc_score = roc_auc_score(y_test, pred_prob[:,1])
    
    # roc curve for tpr = fpr (AUC = 0.5)
    random_probs = [0 for i in range(len(y_test))]
    p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)
    
    plt.rcParams["figure.figsize"] = (5,5)

    ax = plt.subplots()
    ax = sns.lineplot(x=p_fpr, y=p_tpr, color='r')
    ax = sns.lineplot(x=fpr, y=tpr, color='b',linestyle='dashed')
    ax.set(xlabel="False Positive Rate", ylabel="True Positive Rate")
    plt.text(0.5, -0.17, 'AUC Score : '+ str(round(auc_score,2)) , transform=plt.gca().transAxes, ha='center')
    plt.show()
    
# Print confusion matrix and performance metrics
def print_model_performance(model_name,model,X_test,y_test):
    
    display(Markdown("<h2> "+model_name+" </h2>"))
    y_pred = model.predict(X_test)
    
    display(Markdown("<h3> Classification report : </h3>"))
    print(classification_report(y_test,y_pred))
    
    display(Markdown("<h3> Confusion matrix : </h3>"))
    print_confusion_matrix(y_test,y_pred)
    
    display(Markdown("<h3> AUC-ROC Curve : </h3>"))
    plot_auc_roc_curve(model,X_test,y_test)
    
    display(Markdown("<br/>"))

# Get model performance
def get_model_performance(model_name,model,X_test,y_test):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)
    
    precision = round(precision_score(y_test,y_pred,average = "macro"),2)
    recall = round(recall_score(y_test,y_pred,average = "macro"),2)
    auc = round(roc_auc_score(y_test,y_prob[:,1]),2)
    l_loss = round(log_loss(y_test,y_prob),3)
    f1 = round(f1_score(y_test,y_pred,average = "macro"),2)
    accuracy = round(accuracy_score(y_test,y_pred),2)
    
    performance_metrics = {
        "model":model_name,
        "precision_macro":precision,
        "recall_macro":recall,
        "auc":auc,
        "log_loss":l_loss,
        "f1_macro":f1,
        "accuracy":accuracy,
    }
    return performance_metrics

# Get best model based on random search with stratified K Fold
def get_best_model_randomized_search_cv(model_name,model,hyper_params,X_train,y_train):
    cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=1, random_state=1)
    
    print(model_name," :\n")
    
    random_search_cv = RandomizedSearchCV(model, hyper_params, random_state=42,scoring='f1_macro',cv=cv)
    search = random_search_cv.fit(X_train,y_train)
    best_model = search.best_estimator_
    
    print("Best Score :")
    print(round(search.best_score_,2),"\n")
    
    print("Best parameters :")
    print(search.best_params_)
    print("\n")
    
    return best_model
