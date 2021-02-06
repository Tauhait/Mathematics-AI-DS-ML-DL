# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:49:47 2021

@author: TUHIN
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
    
def sim():
    np.random.seed(0)
    n_rvs = 3
    mean = 34/221
    std = np.sqrt(6800/48841)
    p_x = np.array([np.float64(188/221), np.float64(32/221), np.float64(1/221)])
    sim_len = int(1e9)
    sim_counter = np.zeros(shape=n_rvs, dtype=int)
    sim_pmf = np.zeros(shape=n_rvs, dtype=float)
    sim_cdf = np.zeros(shape=n_rvs, dtype=float)
    remain_samples = sim_len
    for i in range(n_rvs):
        sim_bern_arr = bernoulli.rvs(size=remain_samples, p=p_x[i])    
        sim_counter[i] = np.count_nonzero(sim_bern_arr==1)        
        sim_pmf[i] = np.float64(sim_counter[i]/remain_samples)
        remain_samples = remain_samples - sim_counter[i]
    
    sim_cdf = np.cumsum(sim_pmf)
    x = np.array([0, 1, 2])
    y1 = np.array([0.851, 0.145, 0.004])
    y2 = np.array([0.851, 0.996, 1.0])
    print('The simulation PMf values are: ', np.round(sim_pmf, 3))
    print('The CDF values are: ', np.round(sim_cdf, 3))
    plot(x, y1, sim_pmf, mean, std, 'blue', 'red', 'Theory Vs Simulation PMf', False)
    print('\n\n')
    plot(x, y2, sim_cdf, mean, std, 'yellow', 'black', 'Theory Vs Simulation CDF', True)

def plot(x, dist1, dist2, mean, std, col1, col2, t, flag_):    
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

sim()