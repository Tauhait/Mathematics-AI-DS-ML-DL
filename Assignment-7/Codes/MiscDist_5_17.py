# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:43:35 2021

@author: TUHIN
"""
import numpy as np

def mathematical():
    print('Mathematical Results: ')
    print()
    # P(A)
    print('P(A) = ', 1/3)
    # P(A_c)
    print('P(A_c) = ', 2/3)
    # P(B|A)
    print('P(B|A) = ', 3/8)
    # P(B|A_c)
    print('P(B|A_c) = ', 1/2)
    # P(A_c|B)
    print('P(A_c|B) = ', 8/11)
    print()
    print()


def simulation(sim_len):
    rv = np.random.randint(low=1, high=7, size=sim_len)
    count_one_four = len(np.where(rv <= 4)[0])
    count_five_six = len(np.where(rv > 4)[0])
    coin_toss_fiveSix = np.random.binomial(n=3, p=0.5, size=count_five_six)
    coin_toss_oneFour = np.random.binomial(n=1, p=0.5, size=count_one_four)
    print()
    print('Simulation Results: ')
    print()
    # P(A)
    p_five_six = count_five_six/sim_len
    print('P(A) = ', p_five_six)
    
    # P(A_c)
    p_one_four = count_one_four/sim_len
    print('P(A_c) = ', p_one_four)
    
    head_coinTossedThrice = len(np.where(coin_toss_fiveSix==1)[0])
    
    head_coinTossedOnce = len(np.where(coin_toss_oneFour==1)[0])
    
    # P(B|A)
    p_head_coinTossedThrice = head_coinTossedThrice/count_five_six
    print('P(B|A) = ', p_head_coinTossedThrice)
    
    # P(B|A^c)
    p_head_coinTossedOnce = head_coinTossedOnce/count_one_four
    print('P(B|A_c) = ', p_head_coinTossedOnce)
    
    # P(A^c|B) = P(A^c)*P(B|A^c) / P(A^c)*P(B|A^c) + P(A)*P(B|A) 
    p_oneFour_given_oneHead = (p_one_four*p_head_coinTossedOnce)/((p_one_four*p_head_coinTossedOnce) + p_five_six*p_head_coinTossedThrice)
    print('P(A_c|B) = ', p_oneFour_given_oneHead)
    
mathematical()
simulation(10000)