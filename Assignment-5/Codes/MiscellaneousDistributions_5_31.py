# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:49:47 2021

@author: TUHIN
"""
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import binom
    
def sim(precision, num_rvs_gen):
    n_rv = 3
    p_x1 = np.float64(188/221)
    p_x2 = np.float64(32/221)
    p_x3 = np.float64(1/221)
    
    prec = precision
    rvs_size = num_rvs_gen
    sim_len = int(math.pow(10, prec))
    
    sim_bern_arr = np.zeros(shape=(n_rv, rvs_size), dtype=int)
    
    sim_bern_arr[0] = binom.rvs(n=sim_len, p=np.round(p_x1, prec), size=rvs_size)
    sim_bern_arr[1] = binom.rvs(n=sim_len, p=np.round(p_x2, prec), size=rvs_size)
    sim_bern_arr[2] = binom.rvs(n=sim_len, p=np.round(p_x3, prec), size=rvs_size)
    
    sim_pmf = np.zeros(shape=n_rv, dtype=np.float64)
    sim_cdf = np.zeros(shape=n_rv, dtype=np.float64)
    for i in range(n_rv):        
        sim_pmf[i] = np.round(sim_bern_arr[i].mean()/sim_len, prec)
    
    sim_cdf = np.cumsum(sim_pmf)
    x = np.array([0, 1, 2])
    y1 = np.array([np.round(p_x1, prec), np.round(p_x2, prec), np.round(p_x3, prec)])
    y2 = np.array([y1[0], y1[0]+y1[1], y1[0]+y1[1]+y1[2]])
    print('Precision is set to ', prec, ' digits.\n')
    print('The theoretical PMf values are: ', y1)
    print('The simulation PMf values are: ', sim_pmf)
    print('\nThe theoretical CDF values are: ', y2)
    print('The simulated CDF values  are: ', sim_cdf)
    plot(x, y1, sim_pmf, 'blue', 'red', 'Theory Vs Simulation PMf', False)
    print('\n\n')
    plot(x, y2, sim_cdf, 'yellow', 'black', 'Theory Vs Simulation CDF', True)

def plot(x, dist1, dist2, col1, col2, t, flag_):    
    if flag_ is True:
        plt.plot(x, dist2, color='green', marker='o', markersize=12, label='Simulation')
        plt.plot(x, dist1, color='blue', marker='o', markersize=6, label='Theory')
    else:
        plt.stem(x, dist2, linefmt='C1-', markerfmt='C1o', label='Simulation')
        plt.stem(x, dist1, linefmt='C0-', markerfmt='C0.', label='Theory')
    
    plt.grid(color='y', linestyle='--', linewidth=2)
    plt.legend()
    plt.title(t)
    plt.show()

sim(4, int(1e5))