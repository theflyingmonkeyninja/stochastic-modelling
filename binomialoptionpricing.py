#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:14:06 2020

@author: jay
"""

import numpy as np


s = 12; sig = 0.05; r = 0.06; n = 3; T =3; 
optnType = 'call' 
K = 11.1

Op,st = binomialoptionpricing(s,K,sig,r,n,T,optnType)

def binomialoptionpricing(s,K,sig,r,n,T,optnType):
	deltaT = T/n;
	u = np.exp((sig*np.sqrt(deltaT)));
	d = np.exp(-(sig*np.sqrt(deltaT)));
	a = np.exp((r*(deltaT)));
	p = (a-d)/(u-d);
	q = 1-p;
	S = np.zeros([n+1,n+1])
	
	for i in range(n+1):
		for j in range(i+1):
			S[j,i]= s*(u**(i-j))*(d**j);


	optn = np.zeros([n+1,n+1])
	if optnType == 'call':
		optn[:,n] = np.maximum(np.zeros(n+1),(S[:,n]-K))
	else:
		optn[:,n] = np.maximum(np.zeros(n+1),(K-S[:,n]))

	for i in range(n-1,-1,-1):
		for j in range(0,i+1):
			optn[j,i] = (1/(1+r)*(p*optn[j,i+1]+q*optn[j+1,i+1]))
	
	return optn,S


 	

      
    







   
    
   