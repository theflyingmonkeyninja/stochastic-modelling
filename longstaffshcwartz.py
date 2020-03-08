#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:12:54 2020

@author: jay
"""

# =============================================================================
#the longstaff-schwartz montecarlo algorithm is used to find the pricing of an 
# american style option with multiple excercise points. It is a backward induction
# algorithm It computes a continuation  value at each step (the value of option 
# on non-excercise) and compares with intrinsice value to make a decision of excercising 
# or not excercising the option. It uses regression on state variables to compute the
# continuation value.  
# =============================================================================
# S is simulated stock price matrix 
# OPtType is a string of option type
# K is strike # r is riskfree rate

import numpy as np

# europen option price 
def Optionprice(S,K,r,OptType):
    T = np.size(S,1);
    
    if (OptType == 'Eucall'):
        Payoff = np.max((S[:,-1]-K,0));
    else:
        Payoff = np.max((K-S[:,-1],0));
     
    OptPrice = np.mean(Payoff*np.exp(-r*T));   
    
    return OptPrice;


def LSOptionprice(S,K,r,OptType):
    
    T = np.size(S,1);
    excond = np.zeros((np.size(S,0),np.size(S,1)),int);#matrix to store exercise condition
    Payoff =  np.zeros((np.size(S,0),np.size(S,1)),float);
    
    if (OptType == 'Amcall'):
        for i in range (np.size(S,0)):
            for j in range (np.size(S,1)):
                Payoff[i,j] = np.max(S[i,j]-K,0);
            
        
        for i in range(np.size(S,0)):
            if Payoff[i,-1]>0:
                excond[i,-1]=1;
        
    else:
        
        for i in range (np.size(S,0)):
            for j in range (np.size(S,1)):
                Payoff[i,j] = np.max(K-S[i,j],0);
        
        
        for i in range(np.size(S,0)):
            if Payoff[i,-1]>0:
                excond[i,-1]=1;
    
    
    
    for i in range(T,1,-1):
        Y = Payoff[:,i]*np.exp(-r);
        X = S[:,i-1];
        # need to regress Y on X;
        z = np.polyfit(X, Y, 2)
        CV = z[1]*X**2+z[2]*X+z[3];
        for j in range(np.size(S,0)):
            if CV[i]>Payoff[:,i-1]:
                excond[i-1,j]=0;
                
            else:
                excond[i-1,j]=1;
                if excond[i-1,j]==1:
                    excond[i,j]=0;
        
        indx = np.argwhere(excond == 1); #indices of non zero payments
        
        OptPrice = 0
        for i in range(np.size(indx,0)):
            OptPrice = OptPrice+Payoff[indx[i,0],indx[i,1]];
        
        
    return OptPrice, excond;
    
    
# =============================================================================
# Example verification from longstaff paper
# =============================================================================
    S = np.array([[1,1.09,1.08,1.34],[1,1.16,1.26,1.54],[1,1.22,1.07,1.03],[1,.93,.97,.92],[1,1.11,1.56,1.52],[1,.76,.77,.90],[1,.92,.84,1.01],[1,.88,1.22,1.34]]);
    OptType = ''; r =.06; K= 1.10;
    
    price, exmat = LSOptionprice(S,K,r,OptType)