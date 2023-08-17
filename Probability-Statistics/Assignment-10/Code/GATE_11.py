# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:47:57 2021

@author: TUHIN
"""

import numpy as np

sim_len = int(1e6)
X = np.random.randint(low=1, high=101, size=sim_len, dtype=int)
condition = [(np.mod(X, 2) != 0) & (np.mod(X, 3) != 0) & (np.mod(X, 5) != 0)]
Y = np.extract(condition, X)
Pr_Y = Y.size/sim_len
print('The Probability that a given positive integer lying between 1 and 100'
      ' (both inclusive) is NOT divisible by 2, 3 or 5 is - \n')
print('Mathematically Probabity = ', 0.26)
print('Simulated  Probabity = ', Pr_Y)
