# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:49:47 2021

@author: TUHIN
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import bernoulli

def sim(prec):
    n_rv = 3
    x = np.array([0, 1, 2])    
    pmf = np.array([round(188/221, prec), round(32/221, prec), round(1/221, prec)])
    cdf = np.cumsum(pmf)

    sim_len = int(math.pow(10, prec))
    sim_bern_arr = np.zeros(shape=(n_rv, sim_len), dtype=int)
    sim_pmf = np.zeros(shape=n_rv, dtype=float)
    sim_cdf = np.zeros(shape=n_rv, dtype=float)
    sim_counter = np.zeros(shape=n_rv, dtype=int)
    
    for i in range(n_rv):
        sim_bern_arr[i] = bernoulli.rvs(size=sim_len, p=cdf[i])
        sim_counter[i] = np.count_nonzero(sim_bern_arr[i])
        
    sim_counter[1:] -= sim_counter[:-1].copy()
    sim_pmf = np.round(sim_counter/sim_len, prec)
    sim_cdf = np.cumsum(sim_pmf)
    
    print('Precision is set to ', prec, ' digits.\n')
    print('The theoretical PMf values are: ', pmf)
    print('The simulation PMf values are: ', sim_pmf)
    print('\nThe theoretical CDF values are: ', cdf)
    print('The simulated CDF values  are: ', sim_cdf)
    plot(x, pmf, sim_pmf, 'blue', 'red', 'Theory Vs Simulation PMf', False)
    print('\n\n')
    plot(x, cdf, sim_cdf, 'yellow', 'black', 'Theory Vs Simulation CDF', True)

def plot(x, dist1, dist2, col1, col2, t, flag_):    
    if flag_ is True:
        plt.plot(x, dist2, color='green', marker='o', markersize=12, label='Simulation')
        plt.plot(x, dist1, color='blue', marker='o', markersize=6, label='Theory')
    else:
        plt.stem(x, dist2, linefmt='C1-', markerfmt='C1o', label='Simulation')
        plt.stem(x, dist1, linefmt='C0-', markerfmt='C0.', label='Theory')
    for i in range(x.size):
        point_val = "( {}, {} )"
        point_val.format(dist1[i], dist2[i])
        plt.text(x[i], dist2[i], str(point_val.format(dist1[i], dist2[i])), bbox=dict(facecolor='red', alpha=0.1))
        
    plt.grid(color='y', linestyle='--', linewidth=2)
    plt.legend()
    plt.title(t)
    plt.show()

sim(4)