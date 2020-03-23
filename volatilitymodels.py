#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:21:35 2020

@author: jay
"""

#### %%%historical simulation, EWMA, GARCH, ARMA  

import yfinance as yf  
import numpy as np     
import pyflux as pf
import matplotlib.pyplot as plt

def historicalvolatility(s):
         
    l = len(s);
    ind = int(.01*l);
    
    ret = np.log10(s[1:]/s[:-1]); 
    
    sortret = np.sort(ret);
    
    histrisk = ret[ind]
    
    
    paramrisk = -2.33*np.std(ret);
    
    if paramrisk != histrisk:
        print ('gaussian distribution of returns is not correct assumption')
             
    
    
    return paramrisk, histrisk,sortret,ret;


def GarchVol(ret):
	model = pf.GARCH(ret,p=1,q=1);
	x = model.fit();
	assert(len(model.latent_variables.z_list) == 4);
	lvs = np.array([i.value for i in model.latent_variables.z_list]);
	assert(len(lvs[np.isnan(lvs)]) == 0)
	return x, model


# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
st1 = yf.download('^NYA','2017-01-01','2020-3-23')
s = st1.to_numpy(); 
s = s[:,2]; r = np.log10(s[1:]/s[:-1]); 
p,h,sr,r = historicalvolatility(s)

#plt.hist(r)

x, model = GarchVol(r)
print(x.summary())

plt.plot(r);
plt.show();

plt.plot((r**2));
plt.show();

model.plot_fit();