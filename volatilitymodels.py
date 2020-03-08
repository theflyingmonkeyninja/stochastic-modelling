#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:21:35 2020

@author: jay
"""

# historical simulation, EWMA, GARCH, ARMA  

import yfinance as yf  
import numpy as np     
import matplotlib.pyplot as plt

def historicalvolatility(s):
         
    l = np.size(s,0);
    ind = int(.01*l);
    
    ret = np.log10(s[1:]/s[:-1]); 
    
    ret = np.sort(ret);
    
    histrisk = ret[ind]
    
    
    paramrisk = -2.33*np.std(ret);
    
    if paramrisk != histrisk:
        print 'gaussian distribution of returns is not correct assumption'
        
        
    
    
    return paramrisk, histrisk,ret;





# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
st1 = yf.download('TSLA','2014-01-01','2020-01-01')
s = st1.to_numpy(); s = s[:,2];
p,h,r = historicalvolatility(s)

plt.hist(r)