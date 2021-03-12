# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:59:17 2021

@author: TUHIN
"""
import numpy as np
import math
def is_valid_probability_dist(var):
    x = np.zeros((var))
    p_x = np.zeros((var))
    for i in range(var):
        x[i] = float(input('Enter value of x: '))
        p_x[i] = float(input('Enter value of P(x): '))
        if p_x[i] < 0 or p_x[i] > 1.0:
           print('Probability of any event should be between 0 to 1, so it is an')
           return False
    p_sum = math.fsum(p_x)
    print('Summation of  P(x) over the sample space = ', p_sum)
    if p_sum != 1.0:
        print('Since it is not summing up to 1.0, so it is an')
        return False
    return True

def driver():
    obv = input('Enter number of observations: ')
    valid = is_valid_probability_dist(int(obv))
    if valid:
        print('Valid distribution')
    else:
        print('Invalid distribution')
    
    
driver()