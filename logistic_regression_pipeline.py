# Pipeline

features = df.drop(['diagnosis'], axis = 1)
labels = df['diagnosis']

label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)

features = np.array(features)
labels = np.array(labels)

xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size = 0.2,
                                               stratify = labels, random_state = True)

def K_fold(xtrain, ytrain, estimator):
    fold_k = StratifiedKFold(n_splits = 20).split(xtrain, ytrain)
    xtrain_f, xvalid_f,ytrain_f, yvalid_f = [], [], [], []
    for k , (train, valid) in enumerate(fold_k):
        xtrain_f.append(xtrain[train]), xvalid_f.append(xtrain[valid])
        ytrain_f.append(ytrain[train]), yvalid_f.append(ytrain[valid])
        estimator.fit(xtrain[train], ytrain[train])
        st = 'k: {}, train acc: {}, and validation acc: {}'.format(k, estimator.score(xtrain[train], ytrain[train]),
                                                           estimator.score(xtrain[valid], ytrain[valid]))
        print(st)
    return xtrain_f, xvalid_f,ytrain_f, yvalid_f


logistic_regression_pipe = make_pipeline(
    RobustScaler(),
    KernelPCA(kernel = 'rbf', n_components = 20),
    LogisticRegression(solver = 'lbfgs',C = 100, random_state = 1, multi_class = 'ovr',
                      class_weight = 'balanced', max_iter = 3000)
)

param_range = [0.00001, 0.0001, 0.001, 0.01, 0.1, 10, 50, 100, 1000]
train_scores , validation_scores = validation_curve(estimator = logistic_regression_pipe,
                                                   X = xtrain, y = ytrain,
                                                   param_name = 'logisticregression__C',
                                                   param_range = param_range,
                                                   scoring = 'accuracy',
                                                   cv = 10)

plt.plot(param_range, np.max(train_scores, axis = 1), label = 'training accuracy')
plt.plot(param_range, np.max(validation_scores, axis = 1), label = 'validation accuracy')
plt.legend()
     
logisticregression_search = GridSearchCV(
                                        scoring = 'accuracy',
                                        estimator = logistic_regression_pipe,
                                        param_grid = [{
                                            'logisticregression__solver': ['lbfgs', 'liblinear'],
                                            'logisticregression__C': param_range
                                        }],
                                        cv = 10)
logisticregression_search.fit(xtrain, ytrain)

logisticregression_search.best_score_
logisticregression_search.best_params_
logistic_regression_pipe = logisticregression_search.best_estimator_
xtrain_f, xvalid_f,ytrain_f, yvalid_f = K_fold(xtrain,
                                               ytrain,
                                               logistic_regression_pipe)
index = 3
xtraining, ytraining, xvalid, yvalid = xtrain_f[index], ytrain_f[index], xvalid_f[index], yvalid_f[index]
logistic_regression_pipe.fit(xtrain, ytrain)
len(xtraining), len(xvalid)
logistic_regression_pipe.score(xtraining, ytraining)
logistic_regression_pipe.score(xvalid, yvalid)
logistic_regression_pipe.score(xtest, ytest)
y_pred = logistic_regression_pipe.predict(xtest)
y_pred
accuracy_score(y_pred, ytest)*100
print(classification_report(y_pred, ytest))
sns.heatmap(confusion_matrix(y_pred, ytest), annot = True, cmap = 'Blues')
