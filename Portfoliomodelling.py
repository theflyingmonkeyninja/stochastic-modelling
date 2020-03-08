#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:26:05 2020

@author: jay
"""
## s1 and s2 are the returns on the stocks mu1 and mu2 are mean of returns
## the following script can be used to construct markowitz efficient frontier of risky assets

import numpy as np

def cov(s1,mu1,s2,mu2):

    if len(s1)!= len(s2):
        
        print 'error stock returns should have same length' 

    cov = 0;    
    
    for i in range(1,len(s1)):

        cov = cov+(s1[i]-mu1)*(s2[i]-mu2);
    
    cov = cov/(len(s1)-1)
    
    return cov

## s stock values
def returns(s):
         
    ret = np.log10(s[1:]/s[:-1]); 
    
    ESrisk = np.std(ret);
    
    ESret = np.mean(ret);
    
    return ESrisk, ESret,ret;

# w is weights associated to the stocks and ret is the vector of return of stocks
def Portfolioreturns(ret):
    # weights of the assets
    if len(ret) == 2:
        w1 = np.linspace(0,1,1000);
        w2 = 1-w1;
        EPFret = np.multiply(w1,ret[0])+np.multiply(w2,ret[1]);
        wts = [w1,w2];
    else:
        # weights such that their column sum is 1 where column size is given by len(ret)
        wts = np.random.dirichlet(np.ones(len(ret)),size=1000);
                
        for i in range(1,len(ret)):
            
            EPFret = np.dot(wts,ret);
   
        
    return EPFret,wts;

# computing porfolio risk by use of formula \sigma(aX+bY) = \sqrt(a^2 \sigma(X)^2+b^2 \sigma(Y)^2+2ab \sigma(X,Y)
# risk is vector of riskyness of assets and cov is covariance between assets
def Portfoliorisk(wts,risk,cov):
    if len(risk)==2:
        w1 = np.linspace(0,1,1000);
        w2 = 1-w1;
        
        EPFrisk = np.sqrt((np.multiply(w1,risk[0]))**2+2*cov*w1*w2+(np.multiply(w2,risk[1])**2)); 
    else:
        
        
        # sum of w^2\sigma^2
        sigmaii = np.dot(wts**2,risk**2);
    
        j = 1;
        sigmaij = np.zeros((1000,len(risk)),float) 
        for i in range(len(risk)):
            if i<j:
                sigmaij[:,i]=wts[:,i]*wts[:,j]*cov[i,j];
                if j==len(risk):
                    j=0;
                    
                j = j+i;
       
        sigmaij = np.sum(sigmaij,1);
               
        EPFrisk = np.sqrt(sigmaii+sigmaij);    
        
    return EPFrisk
        
    
    
    

    
### launcher file
# Install yfinance package.
#pip install yfinance
     
# Import yfinance
import yfinance as yf  
     
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
st1 = yf.download('MSFT','2018-01-01','2020-01-01')
st2 = yf.download('NFLX','2018-01-01','2020-01-01')
st3 = yf.download('GE','2018-01-01','2020-01-01')
st4 = yf.download('AMZN','2018-01-01','2020-01-01')
st5 = yf.download('GE','2018-01-01','2020-01-01')

 
stock1 = st1.to_numpy(); stock1 = stock1[:,2];
stock2 = st2.to_numpy(); stock2 = stock2[:,2];
stock3 = st3.to_numpy(); stock3 = stock3[:,2];    
stock4 = st4.to_numpy(); stock4 = stock4[:,2];    
stock5 = st5.to_numpy(); stock5 = stock5[:,2];    


# Plot the close prices
import matplotlib.pyplot as plt
st1.Close.plot()
plt.show() 

st2.Close.plot()
plt.show() 

st4.Close.plot()
plt.show() 

st5.Close.plot()
plt.show()

s1risk, s1ret, slret1 = returns(stock1);
s2risk, s2ret, slret2 = returns(stock2);
s3risk, s3ret, slret3 = returns(stock3);
s4risk, s4ret, slret4 = returns(stock4);
s5risk, s5ret, slret5 = returns(stock5);
    

c12 = cov(slret1,s1ret,slret2,s2ret);
c13 = cov(slret1,s1ret,slret3,s3ret);
c14 = cov(slret1,s1ret,slret4,s4ret);
c32 = cov(slret3,s3ret,slret2,s2ret);
c42 = cov(slret4,s4ret,slret2,s2ret);
c43 = cov(slret4,s4ret,slret3,s3ret);

## the covariance matrix can also be obtained by taking svd of AA^T where A is the matrix of stocksxreturns
Cov = np.array([[1, c12, c13, c14],[c12, 1, c32 ,c42],[c13, c32, 1, c43],[c14, c42, c43, 1]]); 

Risk = np.array([s1risk, s2risk, s3risk, s4risk]); 
Ret  = np.array([s1ret, s2ret, s3ret, s4ret]);

#Cov = c12;
#Risk = [s1risk,s2risk]; 
#Ret  = [s1ret,s2ret];


## geting portfolio risk and return
PFRet, swts = Portfolioreturns(Ret);
PFRisk = Portfoliorisk(swts,Risk,Cov); 
        
      
plt.plot(np.transpose(PFRisk), np.transpose(PFRet))
        
    
    
    
    