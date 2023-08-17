import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

sim_len = int(1e2)
X = binom.rvs(n=6, p=0.5, size=sim_len)
X_count = np.zeros(6)
for i in range(6):
    X_count[i] = np.count_nonzero(X == i)
N = 6 * np.ones(sim_len)
Y = N - X
Y_count = np.zeros(6)
for i in range(6):
    Y_count[i] = np.count_nonzero(Y == i)
Z = X - Y
Z_count = np.zeros(7)
y_range = [-6, -4, -2, 0, 2, 4, 6]
for i in range(6):
    Z_count[i] = np.count_nonzero(Z == y_range[i])
plt.stem(X, markerfmt='C0o', label='X = # Heads')
plt.stem(Y, linefmt='C1--', markerfmt='C1.', label='Y = # Tails')
plt.legend()
plt.xlabel('Simulation #')
plt.ylabel('Heads/Tails in n=6 trials')
plt.title('Plot showing # Heads Vs # Tails')
plt.show()
plt.stem(Z, linefmt='C2:', markerfmt='C2*', label='Z = # Heads - # Tails')
plt.xlabel('Simulation #')
plt.ylabel('Heads - Tails in n=6 trials')
plt.title('Plot showing # Heads - # Tails')
plt.legend()
plt.show()