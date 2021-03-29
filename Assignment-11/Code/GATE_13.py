# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:04:54 2021

@author: TUHIN
"""
import matplotlib.pyplot as plt
import numpy as np

trials = int(1e5)
X = np.random.geometric(p=0.166, size=trials)
Pr_X = np.zeros((int(trials/2)))
for i in range(int(trials/2)):
    Pr_X[i] = np.count_nonzero(X == (i*2 + 1))
    Pr_X[i] = Pr_X[i]/trials

Pr_A_win = np.sum(Pr_X)
Pr_X_theo = [1/6, 22/216, 625/7776, 15625/279936]
trials = [1, 3, 5, 7]
print('Simulated Pr(On 1st trial die rolls a six by A) = ', Pr_X[0])
print('Mathematical Pr(On 1st trial die rolls a six by A) = ', 1/6)
print('\n')
print('Simulated Pr(On 3rd trial die rolls a six by A) = ', Pr_X[1])
print('Mathematical Pr(On 3rd trial die rolls a six by A) = ', 25/216)
print('\n')
print('Simulated Pr(On 5th trial die rolls a six by A) = ', Pr_X[2])
print('Mathematical Pr(On 5th trial die rolls a six by A) = ', 625/7776)
print('\n')
print('Simulated Pr(On 7th trial die rolls a six by A) = ', Pr_X[3])
print('Mathematical Pr(On 7th trial die rolls a six by A) = ', 15625/279936)
print('\n')
print('Simulated Pr(A = win) = ', Pr_A_win)
print('Mathematical Pr(A = win) = ', 6/11)
plt.stem(trials, Pr_X[0:4], linefmt='C1--', markerfmt='C1o', label='Sim')
plt.stem(trials, Pr_X_theo, linefmt='C2--', markerfmt='C2.', label='Math')
plt.legend()
plt.xlabel('Trial #')
plt.ylabel('Pr(A rolling six)')
plt.title('Math Vs Sim Pr(A winning the game on odd $k^{th}$ trial)')
plt.show()