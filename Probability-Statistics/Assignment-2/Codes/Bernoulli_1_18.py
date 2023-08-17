# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


#Return probability of Sangeeta winning
def prob_sangeeta_won():
    return 0.62

#Return actual probability of Reshma winning
def prob_reshma_won():    
    return 1 - prob_sangeeta_won()

#Plots the bernoulli distribution
def plot_bernoulli():
    prob_arr = np.array([prob_reshma_won(), prob_sangeeta_won()])
    plt.bar([1, 0], height = prob_arr, align = 'center', color = ['blue', 'red'])
    plt.xticks([1, 0], ['Reshma', 'Sangeeta'])
    plt.xlabel('Players')
    plt.ylabel('Probability of Winning')
    plt.title('Bernoulli Distribution')
    plt.ylim(0, 1)
    plt.show()
    
plot_bernoulli()