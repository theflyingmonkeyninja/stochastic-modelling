#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:51:41 2020

@author: jay
"""
# function to generate correlated random variables from uncorelated ones.


import numpy as np


def corRandVar(n,m):
	Z = np.random.randn(n,m);
	mu = np.random.rand(n,1);
	sig = VarCovarMat(n);
	C = np.linalg.cholesky(sig);
	Y = mu+np.dot(C,Z);
	
	return Y;


def VarCovarMat(n):
	M = np.random.randn(n,n);
	M = np.dot(M,np.transpose(M));
	return M;		 
			


 





