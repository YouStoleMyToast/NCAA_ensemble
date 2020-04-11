import pandas as pd
import matplotlib.pyplot as plt 
import random
import time
import sys, os.path
import seaborn as sns
import numpy as np
import sklearn
import sklearn.impute
import sklearn.linear_model
import sklearn.preprocessing 
# import data_handler as dataHandler
import batch_handler as batchHandler
from sklearn.impute import SimpleImputer

heart_data_args = ["age=0,70","chol=100,400","columns=age,chol,trestbps,thalach"]

def get_data(src,method="mean"):
    df = pd.read_csv("./data_center/" + src,index_col=0)
    if method == "mean":
        df = df.fillna((df.mean()))
    elif method == "sum":
        df = df.fillna((df.sum()))
    # imputer = sklearn.impute.SimpleImputer(missing_values=np.nan,strategy='mean')
    # imputer = imputer.fit(df[:,1:])
    # df[:,1:] = imputer.transform(df[:,1:])
    return df

        
def separate_predictors_and_labels( df,predict="fare_amount" ):
    predictors = df.drop(predict,axis=1)
    labels = df[predict].copy()
    return predictors,labels

def scale_predictors(predictors):
    scaler = sklearn.preprocessing.StandardScaler()
    scaler.fit(predictors)
    predictors = scaler.transform( predictors )
    return predictors,scaler

def to_float64(data):
    return data.astype('float64')

def fit(predictors,labels,modelType,alpha=1):
    if modelType == "regression":
        model = sklearn.linear_model.LinearRegression()
    if modelType == "ridge":
        model = sklearn.linear_model.Ridge(alpha=alpha)
    if modelType == "lasso":
        model = sklearn.linear_model.Lasso(alpha=alpha)
    
    scores = sklearn.model_selection.cross_val_score(model, predictors, labels, scoring="neg_mean_squared_error", cv=5, n_jobs=-1)
    #scores = sklearn.model_selection.cross_val_score(reg, predictors, labels, scoring="neg_mean_squared_error", cv=5, verbose=2, n_jobs=-1)
    scores = np.sqrt(-scores)
    print("Scores:\t", scores)
    print("Mean:\t", np.mean(scores))
    print("Std:\t", np.std(scores))
    model.fit(predictors,labels)
    return model

def train(data,label,modelType):
    predictors,labels = separate_predictors_and_labels(data,predict=label)
    predictors = to_float64(predictors)
    labels = to_float64(labels)
    predictors,scaler = scale_predictors(predictors)
    model = fit(predictors,labels,modelType)
    print("Model:\t",model)
    print("Coef:\t",model.coef_)
    print("Intercept:\t",model.intercept_)
    return model,scaler


def fit_gradient_descent_regression( predictors, labels ):
    reg = sklearn.linear_model.SGDRegressor( loss="squared_loss", penalty="l2", max_iter=1000, tol=0.001 )
    reg.fit( predictors, labels )
    return reg

def write_results(results):
    fout = open("./data_center/results.txt","w+")
    fout.write("Id, SalePrice")
    for i in range(len(results)):
        fout.write(str(1461 + i) + "," +str(results[i]) + "\n")
    fout.close()

def validation_test(test_data, model, scaler, label):
    test_predictors_raw, test_labels = separate_predictors_and_labels(test_data,label)
    test_labels = to_float64(test_labels)
    test_predictors_raw = to_float64(test_predictors_raw)
    test_predictors = scaler.transform(test_predictors_raw)
    test_results = model.predict(test_predictors)
    print("Train Test Results:\t",test_results)
    mean_squared_error = sklearn.metrics.mean_squared_error(test_labels,test_results)
    print("MSE:\t" + str(mean_squared_error))
    root_mean_squared_error = np.sqrt(mean_squared_error)
    print( "RMSE:\t" + str( root_mean_squared_error ) )
    # mean_squared_logarithmic_error = np.sqrt(abs(sklearn.metrics.mean_squared_log_error(test_labels,test_results)))
    # print("RMSLE:\t" + str(mean_squared_logarithmic_error))
    return test_results


def test(test_data, model, scaler):
    test_predictors_raw = to_float64(test_data)
    test_predictors = scaler.transform(test_predictors_raw)
    test_results = model.predict(test_predictors)
    print("Test Results:\t",test_results)
    return test_results

def run_regression(train_data,test_data,label,modelType,validation=True,alpha=1):
    model,scaler = train(train_data,label,modelType)
    if validation:
        return validation_test(test_data,model,scaler,label)
    else:
        return test(test_data,model,scaler)

def main(args):
    if len(args) > 2:
        train_filename = args[1]
        test_filename = args[2]
    else:
        train_filename = "training_data.csv"
        test_filename = "validation_data.csv"
    if os.path.exists( "./data_center/" + train_filename ) and os.path.exists( "./data_center/" + test_filename ):
        basename,ext = train_filename.split('.')
        train_data = get_data(train_filename)
        # model,scaler = train(train_data,label="fare_amount")

        # test_data = get_data(test_filename)
        
        # if len(args) > 3 and args[4] == "-test":
        #     test(test_data,model,scaler)
        # else:
        #     validation_test(test_data,model,scaler)
            
    else:
        print("Error Finding Filepath")

    return

    
    # print(model.predict([[44,108,175,0,0]]))

if __name__ == "__main__":
    main(sys.argv)