import pandas as pd
import numpy as np

import project_wrangle as w

import matplotlib.pyplot as plt
import seaborn as sns

import datetime

import warnings
warnings.filterwarnings("ignore")

# working with dates
from datetime import datetime

# to evaluated performance using rmse
from sklearn.metrics import mean_squared_error
from math import sqrt 

# for tsa 
import statsmodels.api as sm

# holt's linear trend model. 
from statsmodels.tsa.api import Holt


def plot_monthly(train, y):
    '''
    This function takes in a train df and the y target and outputs a plot for monthly plot
    Note: enter y as is, no string
    '''
    for i in range (1,13):
        train[train.month==i].y.plot()
        if i==1:
            i='January'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==2:
            i='February'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==3:
            i='March'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==4:
            i='April'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==5:
            i='May'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==6:
            i='June'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==7:
            i='July'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==8:
            i='August'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==9:
            i='September'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==10:
            i='October'
            plt.title('Yearly Average Temperature Change for '+i)
        if i==11:
            i='November'
            plt.title('Yearly Average Temperature Change for '+i)
        elif i==12:
            i='December'
            plt.title('Yearly Average Temperature Change for '+i)

        plt.show()




def evaluate(target_var):
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse


def plot_and_eval(target_var):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. 
    it will als lable the rmse. 
    '''
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label='Train', linewidth=1)
    plt.plot(validate[target_var], label='Validate', linewidth=1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()


def append_eval_df(model_type, target_var):
    '''
    this function takes in as arguments the type of model run, and the name of the target variable. 
    It returns the eval_df with the rmse appended to it for that model and target_var. 
    '''
    rmse = evaluate(target_var)
    d = {'model_type': [model_type], 'target_var': [target_var],
        'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)