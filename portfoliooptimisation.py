# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script for portfolio optmisation that is using cnvxpy library and solve examples from 
Praticle portfolio optmisation by KV Fernando.
"""

# setting up libraries

import numpy as np
import pandas as pd
import matplotlib as plt
import cvxpy as cp
import pandas_datareader as web
from matplotlib.ticker import FuncFormatter
from pypfopt import risk_models
from pypfopt import expected_returns

# getting asset data
tickers = ['BSX','AES','BRK-B','SEE','QQQ','SPY']
thelen = len(tickers)
price_data = []

for ticker in range(thelen):
    prices = web.DataReader(tickers[ticker],start='2019-01-01', end = '2020-06-06', data_source='yahoo')
    price_data.append(prices.assign(ticker=ticker)[['Adj Close']])
    df_stocks = pd.concat(price_data, axis=1)
    
df_stocks.columns=tickers

    
# computing risk and returns
mu = expected_returns.mean_historical_return(df_stocks)#Sample Variance of Portfolio

Sigma = risk_models.sample_cov(df_stocks)


# computing portfolio 

# optimisation functions
def MinimiseRisk(mu,Sigma):
    n = len(mu);
    x = cp.Variable(n);
    A = np.random.randn(n)
    B = np.ones(n)
    
    prob = cp.Problem(cp.Minimize(cp.quad_form(x, Sigma)),
                      [ x >= np.zeros(n),
                       B @ x == 1])
    
    prob.solve()
     
    print("\nThe optimal value is", prob.value)
    print("A solution x is")
    print(x.value)
    print("A dual solution corresponding to the inequality constraints is")
    print(prob.constraints[0].dual_value)
    
    
def MaxReturn(mu,Sigma,x):
    n = len(mu);
    x = cp.Variable(n);
           
    prob = cp.Problem(cp.Minimize(-mu @ x),
                      [ cp.quad_form(x, Sigma) == 0.02])
    
    prob.solve()
     
    print("\nThe optimal value is", prob.value)
    print("A solution x is")
    print(x.value)
    print("A dual solution corresponding to the inequality constraints is")
    print(prob.constraints[0].dual_value)
    
    
def MaxExpRetwRiskAverse(mu,sigma,x,lam):
    n = len(mu);
    x = cp.Variable(n);
    A = np.random.randn(n)
    B = np.ones(n)
    prob = cp.Problem(lam*cp.Minimize((1/2)*cp.quad_form(x, Sigma) + mu @ x),
                 [G @ x <= h,
                  A @ x == b])
    prob.solve()
    
    print("\nThe optimal value is", prob.value)
    print("A solution x is")
    print(x.value)
    print("A dual solution corresponding to the inequality constraints is")
    print(prob.constraints[0].dual_value)
    



    
#def TransCostOPts(mu,Sigma,x):





