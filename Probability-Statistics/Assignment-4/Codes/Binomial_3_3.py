# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:49:44 2021

@author: TUHIN
"""
import matplotlib.pyplot as plt
import numpy as np
from math import factorial as f
from scipy.stats import bernoulli

def binomial(n, p, q, x):
    return f(n) / (f(x) * f(n - x)) * (p ** x) * (q ** ( n - x))

def calc_binom():
    most_likely = -1
    P_most_likely = 0
    pmf_lst = []
    cdf_lst = []
    summ = 0
    for x in range(7):
        temp = binomial(6, 0.5, 0.5, x)
        pmf_lst.append(temp)
        summ = summ + temp
        cdf_lst.append(summ)
        if temp > P_most_likely:
            P_most_likely = temp
            most_likely = x
    theoryPlot(pmf_lst, 'red', 'PMf')
    print('\nThe most likely outcome is when X =  %d\n' %most_likely)
    print('\nThe probability of the most likely outcome  = %f\n' %P_most_likely)
    theoryPlot(cdf_lst, 'green', 'CDF')
    
    
def sim_binom():
    n_rvs = 7
    sim_len = int(1e4)
    sim_bern_arr = np.zeros(shape=(n_rvs, sim_len), dtype=float)
    sim_counter = np.zeros(shape=n_rvs, dtype=float)
    sim_pmf = np.zeros(shape=n_rvs, dtype=float)
    sim_cdf = np.zeros(shape=n_rvs, dtype=float)
    for i in range(n_rvs):        
        sim_bern_arr[i, :] = bernoulli.rvs(size=sim_len, p=binomial(6, 0.5, 0.5, i))
    
    sim_counter = np.sum(sim_bern_arr, axis=1)
    sim_pmf = sim_counter / sim_len
    sim_cdf = np.cumsum(sim_pmf)
        
    x_lst = [0, 1, 2, 3, 4, 5, 6]
    simPlot(x_lst, sim_pmf, 'blue', 'Simulation PMf')
    print('\n\n')
    simPlot(x_lst, sim_cdf, 'yellow','Simulation CDF')


def simPlot(x, dist, col, t):
    plt.bar(x, dist, color=col)
    plt.title(t)
    plt.show()
    
def theoryPlot(Y, col, density):
    x = [0, 1, 2, 3, 4, 5, 6]
    plt.plot(x, Y, color=col, marker='.', linestyle='dotted')
    plt.title('Theoretical ' + density +' distribution of a Binomial RV')
    plt.show()

calc_binom()
sim_binom()