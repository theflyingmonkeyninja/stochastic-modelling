# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:06:00 2020

@author: dhana
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def BlackDermanToyInterestRate(ZCRates,ZCVol,ParVal):
    # this function computes the short rate for BDT model
    # MatPeriod is years to maturity of Zero coupon Bond
    # ZCRate is the zero coupon rate in %
    # ZCVol is the zero coupon Volatility in %
    # FVal face value of ZC-Bond
    
    treelength = len(ZCRates); # length of the binomial tree
    
    ZCBPrice =  np.zeros(treelength+1);# array for Zero coupon bond price
    
    # computing price of Zero Coupon Bond
    for i in range(treelength+1):
        ZCBPrice[i] = ParVal/(1+ZCRates[i-1])**i;
        
    SRate = np.zeros([treelength,treelength]);# matrix of short rate 
   
    ZCBPrice = ZCBPrice[1:];
      
    SRate[0,0] = ZCRates[0];
     
    for i in range(1,treelength):
        
        guess = 0.0787
        bsum = 0
        
    
        while bsum!=ZCBPrice[i]:
            
            Sigma = np.exp(2*ZCVol[i]); 
            bsum = 0;
            Dfact = 1
            
            if  i==1:
                Dfact =1;
            elif i==2:
                Dfact = np.prod(SRate[0,:]+1);
            else:
                for k in range(i-1):
                    Dfact = Dfact* np.prod(SRate[k,:]+1);
            
            
            for j in range(treelength):
                if j<i:
                    bsum = bsum +(0.5**i*ParVal/(1+guess*Sigma**j)+0.5**i*ParVal/(1+guess*Sigma**(j+1)))/(Dfact*(1+SRate[i-1,j]))    
                  
                else:
                    break;
                    
                    
            if np.absolute(bsum-ZCBPrice[i])<0.5:
                 SRate[i,j] = guess;
                 break;
            elif bsum<ZCBPrice[i]:
                guess = (guess-.001);
                if guess<0:
                    print('error')
            elif bsum>ZCBPrice[i]:
                guess = (guess+0.001);
           
        length = j+1;
        Temp = np.zeros(length); 
        m = j;
        
        for k in range(length):            
            Temp[k] = SRate[i,j]*Sigma**m;
            m = m-1
        
        Temp = np.flip(Temp);
        
        for j in range(treelength):
            if j<i+1:
                SRate[i,j] = Temp[j];
            else:
                break;
                
    
    return SRate;      



ZCRates = np.array( [9,9.5,10,10.5,11]);
ZCRates = ZCRates/100;
ZCVol = np.array([24,22,20,18,16]);
ZCVol = ZCVol/100;
ParVal = 100
SRate = BlackDermanToyInterestRate(ZCRates,ZCVol,ParVal);
