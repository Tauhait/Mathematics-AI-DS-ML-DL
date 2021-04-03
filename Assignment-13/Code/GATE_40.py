# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 23:57:20 2021

@author: TUHIN
"""

import numpy as np
sim_len = int(1e5)
X = np.random.binomial(n=3, p=0.1, size=sim_len)
count_X = np.count_nonzero(X == 0) + np.count_nonzero(X == 1)
count_X /= sim_len
print('Simulated Pr(error) = ', 1 - count_X)
print('Mathematically Pr(error) = ', 0.028)