import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Initiaze X to be between 0.1 to 10 with a step of 0.2
X = np.arange(0.1, 10, 0.2)
label = ['$\sigma$ = 0.5', '$\sigma$ = 1.0', '$\sigma$ = 2.0', 
         '$\sigma$ = 3.0', '$\sigma$ = 4.0']
color = ['r-', 'g-', 'c-', 'b-', 'y-']
sigma = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
Y  = np.zeros((5, 50))

# Function returns Probability density of X for given parameter sigma
def calcPDf(x, s):
    return (x / np.power(s, 2)) * exponent(x, s)

# Function returns Probability distribution of X for given parameter sigma
def calcCDF(x, s):
    return 1 - exponent(x, s)

# Utility function used for CDF and PDf calc
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

# Utility distribution function for plotting
def plotDist(xStart, yStart, xLimit, yLimit, labelY):
    plt.legend()
    plt.title('Rayleigh Distribution ' + labelY)
    plt.xlim(xStart, xLimit)
    plt.ylim(yStart, yLimit)
    plt.xlabel('Range of X')
    plt.ylabel(labelY)
    plt.show()

# Utility method to genearate linearly spaced 500 real nos in range(0, 10)
def gene_linspace_x():
    return np.linspace(start=0, stop=10, num=500)

# Verify PDf using simulation
def verify_PDf():
    X = gene_linspace_x()
    ray_pdf = stats.rayleigh.pdf(X, loc=0.0, scale=0.5)
    plot(X, ray_pdf, "red", 'PDf')

# Verify PDf using simulation
def verify_CDF():
    X = gene_linspace_x()
    ray_cdf = stats.rayleigh.cdf(X, loc=0.0, scale=0.5)
    plot(X, ray_cdf, "green", 'CDF')

# Utiltity method to help plotting
def plot(x, y, col, density_type):
    plt.plot(x, y, color=col)
    plt.xlabel('Range of X')
    plt.ylabel(density_type)
    plt.title(density_type + ' plot using derived formula')
    plt.show()  
    
plotPDf()
plotCDF()
verify_PDf()
verify_CDF()