# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:51:54 2021

@author: TUHIN
"""

#Generate samples for two gaussian distributions with non-zero mean and variance.
#show that their addition is also a gaussian random variable 
#with mean as sum of individual means and variance as sum of individual variances.

import numpy as np
import matplotlib.pyplot as plt
from math import pi, e, sqrt

def normal_pdf(x, mean, sigma):
    return (1.0 / sigma*sqrt(2*pi))*pow(e, (-0.5)*((x-mean)/sigma)**2)

def add_two_rv(mew1, mew2, sigma1, sigma2, sim_len):
    rv1 = np.random.normal(mew1, sigma1, sim_len)    
    rv2 = np.random.normal(mew2, sigma2, sim_len)
    
    comb_rv1_rv2 = rv1 + rv2
    theo_comb_mean = np.mean(comb_rv1_rv2)
    theo_comb_std = np.std(comb_rv1_rv2)
    theo_pdf = normal_pdf(comb_rv1_rv2, theo_comb_mean, theo_comb_std)
    
    sim_comb_rv = np.random.normal(mew1 + mew2, np.sqrt(sigma1**2 + sigma2**2), sim_len)
    sim_comb_mean = np.mean(sim_comb_rv)
    sim_comb_sd = np.std(sim_comb_rv)
    sim_pdf = normal_pdf(sim_comb_rv, sim_comb_mean, sim_comb_sd)
    
    print('\nAddition of two RVs mean  - \nTheo: ', theo_comb_mean, '\nSim: ', sim_comb_mean)
    print('\nAddition of two RVs Variance  - \nTheo: ', theo_comb_std**2, '\nSim: ', sim_comb_sd**2)

    plt.scatter(comb_rv1_rv2, theo_pdf, marker ="o", color= 'blue', label='Theoretical')
    plt.scatter(sim_comb_rv, sim_pdf, marker =".", color= 'orange', label='Simulation')
    plt.legend()
    plt.title('Theo Vs Sim PDf of addition of two RVs')
    plt.xlabel('X')
    plt.ylabel('pdf of X')
    plt.show() 
    
add_two_rv(1, 2, 3, 4, int(1e5))    
    
