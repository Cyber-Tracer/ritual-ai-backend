def get_performance_metrics_supervised(model, test_data):
    import pandas as pd
    import tensorflow as tf
    import numpy as np
    import sklearn.metrics as metrics
    import joblib
    
    model = joblib.load(model)
    test_data = pd.read_csv(test_data)
    print("MODEL working")
    print("TEST DATA working")
    
    X_test = test_data.iloc()
    y_test = test_data.reset_index(drop=True).iloc[:, -1]
    y_true = y_test.values.flatten()
    
    if isinstance(model, tf.keras.Sequential):
        y_pred_proba = model.predict(X_test)
        y_pred = np.argmax(y_pred_proba, axis=1)
    else:
        y_pred = model.predict(X_test).flatten()
    
    labels = np.unique(np.array([y_pred, y_true]).flatten())

    dict_performance_metrics = {"accuracy": round(metrics.accuracy_score(y_true, y_pred), 2),
                                "global recall": round(metrics.recall_score(y_true, y_pred, labels=labels, average="micro"), 2),
                                "class weighted recall": round(metrics.recall_score(y_true, y_pred, average="weighted"), 2),
                                "global precision": round(metrics.precision_score(y_true, y_pred, labels=labels, average="micro"), 2),
                                "class weighted precision": round(metrics.precision_score(y_true, y_pred, average="weighted"), 2),
                                "global f1 score": round(metrics.f1_score(y_true, y_pred, average="micro"), 2),
                                "class weighted f1 score": round(metrics.f1_score(y_true, y_pred, average="weighted"), 2)}

    return dict_performance_metrics


model=r"Validation\unsupervised\CBLOF\model.joblib"
test=r"Validation\unsupervised\CBLOF\test.csv"
factsheet=r"Validation\unsupervised\CBLOF\factsheet.json"
a=get_performance_metrics_supervised(model=model,test_data=test)
print(a)