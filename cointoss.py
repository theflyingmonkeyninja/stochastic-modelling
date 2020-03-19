#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:41:56 2020

@author: jay
"""
# monte carlo simulation to compute the fair value of a game of coin tosses
# such that two successive coin tosses are heads.
import numpy as np
nsamps = 1000

def cointoss(nsamps):
    val = np.zeros((nsamps,1));
    for i in range(nsamps-1):
        count = 0
        s = np.random.choice([0,1],100);# 100 coin tosses
        for k in range(98):
            if s[k] == 1 and s[k+1] == s[k]:
                count = count+(k+2); #k+2 because k represent coin toss number +1 is for
                break                # total coin toss and other +1 is for python count 
    
        val[i] = count;
    
    meanval = np.mean(val)
    return meanval;    