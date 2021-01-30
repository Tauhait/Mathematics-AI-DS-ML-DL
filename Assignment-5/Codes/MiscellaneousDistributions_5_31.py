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
    p_x = np.array([188/221, 32/221, 1/221])
    sim_len = int(1e6)
    sim_bern_arr = np.zeros(shape=(n_rvs, sim_len), dtype=float)
    sim_counter = np.zeros(shape=n_rvs, dtype=float)
    sim_pmf = np.zeros(shape=n_rvs, dtype=float)
    sim_cdf = np.zeros(shape=n_rvs, dtype=float)
    for i in range(n_rvs):
        sim_bern_arr[i, :] = bernoulli.rvs(size=sim_len, p=p_x[i])
    
    sim_counter = np.sum(sim_bern_arr, axis=1)
    sim_pmf = sim_counter / sim_len
    sim_cdf = np.cumsum(sim_pmf)
    x = np.array([0, 1, 2])
    y1 = np.array([0.851, 0.145, 0.004])
    y2 = np.array([0.851, 0.996, 1.0])
    plot(x, y1, sim_pmf, mean, std, 'blue', 'red', 'Theory Vs Simulation PMf')
    print('\n\n')
    plot(x, y2, sim_cdf, mean, std, 'yellow', 'black', 'Theory Vs Simulation CDF')

def plot(x, dist1, dist2, mean, std, col1, col2, t):    
    plt.stem(x, dist2, linefmt='C1-', markerfmt='C1o', label='Simulation')
    plt.stem(x, dist1, linefmt='C0-', markerfmt='C0.', label='Theory')
    plt.grid(color='y', linestyle='--', linewidth=2)
    plt.ylim(0, 1.25)
    plt.legend()
    plt.title(t)
    plt.show()

sim()