import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#Initiaze X to be between 0.1 to 10 with a step of 0.2
X = np.arange(0.1, 10, 0.2)
label = ['$\sigma$ = 0.5', '$\sigma$ = 1.0', '$\sigma$ = 2.0', 
         '$\sigma$ = 3.0', '$\sigma$ = 4.0']
color = ['r-', 'g-', 'c-', 'b-', 'y-']
sigma = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
Y  = np.zeros((5, 50))

#Function returns Probability density of X for given parameter sigma
def calcPDf(x, s):
    return (x / np.power(s, 2)) * exponent(x, s)

#Function returns Probability distribution of X for given parameter sigma
def calcCDF(x, s):
    return 1 - exponent(x, s)

#Utility function used for CDF and PDf calc
def exponent(x, s):
    return np.exp(-np.power(x, 2) / (2 * np.power(s, 2)))

# plot PDf
def plotPDf():
    for i in range(5):
        Y[i, :] = calcPDf(X, sigma[i])
        plt.plot(X, Y[i, :], color[i], label=label[i])
    plotDist(0.1, 0, 10, 1.5, 'PDf')

# plot CDF
def plotCDF():    
    for i in range(5):
        Y[i, :] = calcCDF(X, sigma[i])
        plt.plot(X, Y[i, :], color[i], label=label[i])
    plotDist(0.1, 0, 10, 1.0, 'CDF')

#Utility distribution function for plotting
def plotDist(xStart, yStart, xLimit, yLimit, labelY):
    plt.legend()
    plt.title('Rayleigh Distribution ' + labelY)
    plt.xlim(xStart, xLimit)
    plt.ylim(yStart, yLimit)
    plt.xlabel('Range of X')
    plt.ylabel(labelY)
    plt.show()

# Verify PDf using simulation
def simulate_verify_PDf():
    ray_X_rvs = np.random.uniform(low=0, high=10, size=50)
    ray_pdf = stats.rayleigh.pdf(ray_X_rvs, loc=0.0, scale=4.0)
    y = calcPDf(ray_X_rvs, 3.5)
    plt.xlim(0, 10)
    plt.plot(y, color='green')
    plt.plot(ray_pdf, color='red')
    plt.title('Rayleigh Distribution PDf Actual Vs Simulation')
    plt.legend(["Actual", "Simulation"])
    plt.show()

# Verify PDf using simulation
def simulate_verify_CDF():
    ray_X_rvs = np.random.uniform(low=0, high=10, size=50)
    ray_pdf = stats.rayleigh.cdf(ray_X_rvs, loc=0.0, scale=4.0)
    y = calcCDF(ray_X_rvs, 3.5)
    plt.xlim(0, 10)
    plt.plot(y, color='green')
    plt.plot(ray_pdf, color='red')
    plt.title('Rayleigh Distribution CDF Actual Vs Simulation')
    plt.legend(["Actual", "Simulation"])
    plt.show()
    
plotPDf()
plotCDF()
simulate_verify_PDf()
simulate_verify_CDF()