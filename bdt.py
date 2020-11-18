# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:06:00 2020

@author: dhana
"""
import numpy as np


def BlackDermanToyInterestRate(ZCRates,ZCVol,ParVal):
    # this function computes the short rate for BDT model
    # MatPeriod is years to maturity of Zero coupon Bond
    # ZCRate is the zero coupon rate in %
    # ZCVol is the zero coupon Volatility in %
    # ParVal face value of ZC-Bond
    
    treelength = len(ZCRates); # length of the binomial tree
    
    ZCBPrice =  np.zeros(treelength+1);# array for Zero coupon bond price
    
    # computing price of Zero Coupon Bond
    for i in range(treelength+1):
        ZCBPrice[i] = ParVal/(1+ZCRates[i-1])**i;
        
    SRate = np.zeros([treelength,treelength]);# matrix of short rate 
   
    ZCBPrice = ZCBPrice[1:];
      
    SRate[0,0] = ZCRates[0];
     
    for i in range(1,treelength):
        
            
        x = np.zeros(1000);
        x[0] = 0.0;
        x[1] = 0.079;
        
        Sigma = np.exp(2*ZCVol[i]); 
        
        
        for itr in range(2,2000):
            
            # fixing  the intreval for the root
            
            F0 = np.zeros([treelength,treelength]);
            F1 = np.zeros([treelength,treelength]);
       
          
            
            for j in range(treelength):
                if j<=i:
                   
                    F0[i,j] = ParVal/(1+x[itr-2]*Sigma**(j))    
                    F1[i,j] = ParVal/(1+x[itr-1]*Sigma**(j))
                    

                else:
                    break;
             
            for m in reversed(range(i)):
                for n in range (i):
                    if n<=m:
                        F0[m,n] = (0.5*F0[m+1,n]+0.5*F0[m+1,n+1])/(1+SRate[m,n])
                        F1[m,n] = (0.5*F1[m+1,n]+0.5*F1[m+1,n+1])/(1+SRate[m,n])
              
            f0 = F0[0,0]
            f1 = F1[0,0]
            
            f0 = ZCBPrice[i]-f0;
            f1 = ZCBPrice[i]-f1;
                
            
            x[itr] = x[itr-1]-f1*(x[itr-1]-x[itr-2])/(f1-f0);
            
            F = np.zeros([treelength,treelength]);
                        
            for j in range(treelength):
                 if j<=i:
                                      
                     F[i,j] = ParVal/(1+x[itr]*Sigma**(j));
                   
                    
                 else:
                     break;
                     
                     
            for m in reversed(range(i)):
                for n in range (i):
                    if n<=m:
                        F[m,n] = (0.5*F[m+1,n]+0.5*F[m+1,n+1])/(1+SRate[m,n])         
                     
            f = F[0,0];
            f = ZCBPrice[i]-f;
             
                           
            if np.abs(f)<0.000001:
                 SRate[i,i] = x[itr]; 
                 break;
           
          
        length = i+1;
        
        Temp = np.zeros(length); 
        m = i;
        
        for k in range(length):            
            Temp[k] = SRate[i,i]*Sigma**m;
            m = m-1
        
        Temp = np.flip(Temp);
        
        for j in range(treelength):
            if j<i+1:
                SRate[i,j] = Temp[j];
            else:
                break;
                
        
                
    SRate = SRate*100
    return SRate,F;      



# ZCRates = np.array([10,11,12,12.5,13]);
# ZCRates = ZCRates/100;
# ZCVol = np.array([20,19,18,17,16]);
# ZCVol = ZCVol/100;
# ParVal = 100
# SRate = BlackDermanToyInterestRate(ZCRates,ZCVol,ParVal);

# ZCRates = np.array([9,9.5,10,10.5,11]);
# ZCRates = ZCRates/100;
# ZCVol = np.array([24,22,20,18,16]);
# ZCVol = ZCVol/100;
# ParVal = 100
# (F,SRate) = BlackDermanToyInterestRate(ZCRates,ZCVol,ParVal);

ZCRates = np.array([10,11,12,12.5,13]);
ZCRates = ZCRates/100;
ZCVol = np.array([20,19,18,17,16]);
ZCVol = ZCVol/100;
ParVal = 100
(F,SRate) = BlackDermanToyInterestRate(ZCRates,ZCVol,ParVal);


