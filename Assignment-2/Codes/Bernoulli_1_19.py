# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


#Returns probability of no head on two coin tosses, i.e { TT }
def prob_no_head():
    return 1/4

#Returns probability of at least one head on two coin tosses, i.e 1 - P(no head)
def prob_at_least_one_head():    
    return 1 - prob_no_head()

#Plots the bernoulli distribution 
def plot_bernoulli():
    prob_arr = np.array([prob_at_least_one_head(), prob_no_head()])
    plt.bar([1, 0], height = prob_arr, align = 'center', color = ['green', 'yellow'])
    plt.xticks([1, 0], ['At least one Head', 'No Head'])
    plt.xlabel('Heads from two coin tosses')
    plt.ylabel('Probability')
    plt.title('Bernoulli Distribution')
    plt.ylim(0, 1)
    plt.show()
    
plot_bernoulli()