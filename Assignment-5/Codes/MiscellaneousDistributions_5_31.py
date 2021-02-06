# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:49:47 2021

@author: TUHIN
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
    
def sim():
    n_rvs = 3
    mean = 34/221
    std = np.sqrt(6800/48841)
    p_x1 = np.float64(188/221)
    p_x2 = np.float64(32/221)
    p_x3 = np.float64(1/221)
    
    sim_len = int(1e9)
    sim_bern_arr = np.zeros(shape=(n_rvs, sim_len), dtype=int)
    sim_bern_arr[0] = bernoulli.rvs(size=sim_len, p=p_x1)
    sim_bern_arr[1] = bernoulli.rvs(size=sim_len, p=p_x2)
    sim_bern_arr[2] = bernoulli.rvs(size=sim_len, p=p_x3)
    
    sim_counter = np.zeros(shape=n_rvs, dtype=int)
    sim_pmf = np.zeros(shape=n_rvs, dtype=np.float64)
    sim_cdf = np.zeros(shape=n_rvs, dtype=np.float64)
    for i in range(n_rvs):
        sim_counter[i] = np.count_nonzero(sim_bern_arr[i]==1)
        temp = sim_counter[i]/sim_len
        sim_pmf[i] = temp
    
    sim_cdf = np.cumsum(sim_pmf)
    x = np.array([0, 1, 2])
    y1 = np.array([p_x1, p_x2, p_x3])
    y2 = np.array([p_x1, p_x1 + p_x2, p_x1 + p_x2 + p_x3])
    print('The theoretical PMf values are: ', y1)
    print('The simulation PMf values are: ', sim_pmf)
    print('The theoretical CDF values are: ', y2)
    print('The simulated CDF values  are: ', sim_cdf)
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