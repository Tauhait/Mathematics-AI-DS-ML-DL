# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 01:17:43 2021

@author: TUHIN
"""

import numpy as np
from scipy.stats import bernoulli

sim_len = int(1e5)
P_oddno_frst_or_scnd_thw = 0.5
P_odd_no_frst_and_scnd_thw = 0.25

rv_oddno_frstThw = bernoulli.rvs(size=sim_len, p=P_oddno_frst_or_scnd_thw)
rv_oddno_scndThw = bernoulli.rvs(size=sim_len, p=P_oddno_frst_or_scnd_thw)
rv_oddno_bothThw = bernoulli.rvs(size=sim_len, p=P_odd_no_frst_and_scnd_thw)

count_oddno_frstThw = np.count_nonzero(rv_oddno_frstThw == 1)
count_oddno_scndThw = np.count_nonzero(rv_oddno_scndThw == 1)
count_oddno_bothThw = np.count_nonzero(rv_oddno_bothThw == 1)

sim_p_oddno_frstThw = count_oddno_frstThw/sim_len
sim_p_oddno_scndThw = count_oddno_scndThw/sim_len
sim_p_oddno_bothThw = count_oddno_bothThw/sim_len

print('Simulated probability of odd number on the first throw', sim_p_oddno_frstThw)
print('Mathematical probability of odd number on the first throw', P_oddno_frst_or_scnd_thw)
print('\n\nSimulated probability of odd number on the second throw', sim_p_oddno_scndThw)
print('Mathematical probability of odd number on the second throw', P_oddno_frst_or_scnd_thw)
print('\n\nSimulated probability of odd number on the both throw', sim_p_oddno_bothThw)
print('Mathematical probability of odd number on the both throw', P_oddno_frst_or_scnd_thw*P_oddno_frst_or_scnd_thw)