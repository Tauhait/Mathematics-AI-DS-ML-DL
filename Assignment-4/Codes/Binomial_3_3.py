# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:49:44 2021

@author: TUHIN
"""
import matplotlib.pyplot as plt
from math import factorial as f
from scipy.stats import binom

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
    x_lst = [0, 1, 2, 3, 4, 5, 6]
    
    sim_pmf_dist = [binom.pmf(k, n = 6, p = 0.5) for k in x_lst]
    simPlot(x_lst, sim_pmf_dist, 'blue', 'Simulation PMf')
    print('\n\n')
    sim_cdf_dist = [binom.cdf(k, n = 6, p = 0.5) for k in x_lst]
    simPlot(x_lst, sim_cdf_dist, 'yellow','Simulation CDF')


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