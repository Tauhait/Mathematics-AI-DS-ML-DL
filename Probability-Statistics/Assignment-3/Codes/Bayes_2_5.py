# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:59:44 2021

@author: TUHIN
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def bayes_theorem(P_E, P_F_given_E, P_F):
    return (P_E * P_F_given_E) / P_F

def calc_P_F_given_E(P_E_and_F, P_E):
    return P_E_and_F / P_E

def calc_P_E_given_F(P_E_and_F, P_F):
    return P_E_and_F / P_F
    
def bothChildMale_given_at_least_one_male():    
    # Prior or P(E) = both children to be males
    P_E = np.random.random()
    
    # Evidence or P(F) = at least one children to be male
    P_F = np.random.random()
    
    # P(E and F)
    P_E_and_F = P_E * P_F
    
    # Likelihood or P( F|E )
    P_F_given_E = calc_P_F_given_E(P_E_and_F, P_E)
    
    # Posterior or P( E|F )
    P_E_given_F = bayes_theorem(P_E, P_F_given_E, P_F)
    
    return P_E_given_F

def bothChildFemale_given_elder_female():    
    # Prior or P(E) = both children to be females
    P_E = np.random.random()
    
    # Evidence or P(F) = elder child being a female
    P_F = np.random.random()
    
    # P(E and F)
    P_E_and_F = P_E * P_F
    
    # Likelihood or P( F|E )
    P_F_given_E = calc_P_F_given_E(P_E_and_F, P_E)
    
    # Posterior or P( E|F )
    P_E_given_F = bayes_theorem(P_E, P_F_given_E, P_F)
    
    return P_E_given_F

def simulate_bayes_bernoulli():
    P_both_male = bothChildMale_given_at_least_one_male()
    P_both_female = bothChildFemale_given_elder_female()
    
    sim_len = int(1e3)
    
    sim_bern1 = bernoulli.rvs(size=sim_len, p=P_both_male)
    sim_bern2 = bernoulli.rvs(size=sim_len, p=P_both_female)
    
    fav_outcome_both_male = np.nonzero(sim_bern1 == 1)
    fav_outcome_both_female = np.nonzero(sim_bern2 == 1)
    
    p_sim_bern1 = len(fav_outcome_both_male[0])/sim_bern1.size
    p_sim_bern2 = len(fav_outcome_both_female[0])/sim_bern2.size
    
    
    plot(sim_bern1,
      '0 = Second child female                           1 = Second child male',
      'Simulation of Bernoulli Dist. of second child male given first child male')
    print('\n Simulation P( both children male | at least one child male ) = %f\n' % p_sim_bern1)
    print('\n Condtional P( both children male | at least one child male ) = %f\n' % P_both_male)
    print('\n Simulation P( both children female | given that the elder child is a female ) = %f\n' % p_sim_bern2)
    print('\n Condtional P( both children female | given that the elder child is a female ) = %f\n' % P_both_female)
    plot(sim_bern2, 
      '0 = Second child male                           1 = Second child female ',
      'Simulation of Bernoulli Dist. of second child female given first child female')

def plot(data_bern, xl, t):
    ax = sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={'linewidth': 25,'alpha':1})
    ax.set(xlabel=xl, ylabel='Frequency')
    ax.set(title=t)
    plt.show()

simulate_bayes_bernoulli()
