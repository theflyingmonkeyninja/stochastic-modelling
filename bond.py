# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:38:59 2020

@author: dhana
"""

import numpy as np
import matplotlib as plt

Irate = 0.1*np.random.rand(100);# in percentage
Crate = 0.1*np.random.rand(100);# in percentage 
tenor = np.arange (0,5.5,0.5);


Principal = 1000

coupon = Principal*Crate;

Cashflow = np.zeros((len(Crate),len(tenor)));

for i in range(len(Crate)):
    Cashflow[i,:] = coupon[i];
    Cashflow[i,-1] = Cashflow[i,-1]+Principal;
    


M = np.zeros((len(Irate),len(Crate)));

temp1 = np.zeros(len(tenor))
temp2 = np.zeros(len(tenor))

for i in range(len(Irate)):
    for j in range(len(Crate)):
        for k in range(len(tenor)):
            temp1[k] = Cashflow[j,k]/(1+Irate[i])**tenor[k]*tenor[k]
            temp2[k] = Cashflow[j,k]/(1+Irate[i])
        M[i,j] = np.sum(temp1/np.sum(temp2));

       
        
