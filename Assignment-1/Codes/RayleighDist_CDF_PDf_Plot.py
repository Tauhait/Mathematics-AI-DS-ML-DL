import numpy as np
import matplotlib.pyplot as plt

#Initiaze X to be between 0.1 to 10 with a step of 0.2
X = np.arange(0.1, 10, 0.2)

#Function returns Probability density of X for given parameter sigma
def calcPDf(s):
    return (X / np.power(s, 2)) * exponent(s)

#Function returns Probability distribution of X for given parameter sigma
def calcCDF(s):
    return 1 - exponent(s)

def exponent(s):
    return np.exp(-np.power(X, 2) / (2 * np.power(s, 2)))

def plotPDf():    
    sigma = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
    Y0 = calcPDf(sigma[0])
    plt.plot(X, Y0, 'r-', label='$\sigma$ = 0.5')
    
    Y1 = calcPDf(sigma[1])
    plt.plot(X, Y1, 'g-', label='$\sigma$ = 1.0')
    
    Y2 = calcPDf(sigma[2])
    plt.plot(X, Y2, 'c-', label='$\sigma$ = 2.0')
    
    Y3 = calcPDf(sigma[3])
    plt.plot(X, Y3, 'b-', label='$\sigma$ = 3.0')
    
    Y4 = calcPDf(sigma[4])
    plt.plot(X, Y4, 'y-', label='$\sigma$ = 4.0')
    plt.legend()
    plt.title('Rayleigh Distribution PDf')
    plt.xlim(0.1, 10)
    plt.ylim(0, 1.5)
    plt.xlabel('Range of X')
    plt.ylabel('Range of Y')
    plt.show()

def plotCDF():    
    sigma = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
    Y0 = calcCDF(sigma[0])
    plt.plot(X, Y0, 'r-', label='$\sigma$ = 0.5')
    
    Y1 = calcCDF(sigma[1])
    plt.plot(X, Y1, 'g-', label='$\sigma$ = 1.0')
    
    Y2 = calcCDF(sigma[2])
    plt.plot(X, Y2, 'c-', label='$\sigma$ = 2.0')
    
    Y3 = calcCDF(sigma[3])
    plt.plot(X, Y3, 'b-', label='$\sigma$ = 3.0')
    
    Y4 = calcCDF(sigma[4])
    plt.plot(X, Y4, 'y-', label='$\sigma$ = 4.0')
    plt.legend()
    plt.title('Rayleigh Distribution CDF')
    plt.xlim(0.1, 10)
    plt.ylim(0, 1.0)
    plt.xlabel('Range of X')
    plt.ylabel('Range of Y')
    plt.show()

plotPDf()
plotCDF()