import math
import os
import csv
import numpy as np
from scipy.optimize import fsolve
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt

def dPotential1(r, *mus):
    errflg = 0
    #Unpack tuple
    mu1, mu2 = mus
    T1 = 1. - r
    T2 = T1 - 1.0/T1**2
    T3 = r - 1.0/r**2
    dU = mu1*T2 - mu2*T3 # Equation 3.73
    return dU

def dPotential2(r, *mus):
    errflg = 0
    #Unpack tuple
    mu1, mu2 = mus
    T1 = 1. + r
    T2 = T1 - 1.0/T1**2;
    T3 = r - 1.0/r**2;
    dU = mu1*T2 + mu2*T3 #Equation 3.85
    return dU

def dPotential3(r, *mus):
    errflg = 0
    #Unpack tuple
    mu1, mu2 = mus
    T1 = 1. + r
    T2 = r - 1.0/r**2
    T3 = T1 - 1.0/T1**2
    dU = mu1*T2 + mu2*T3 # Equation 3.90
    return dU


def Potential(x, *data):
    #Unpack tuple
    y, z, mu1, mu2, Vref = data
    r1 = math.sqrt((x+mu2)**2 + y**2 + z**2)
    r2 = math.sqrt((x-mu1)**2 + y**2 + z**2)
    T1 = 1.0/r1 + 0.5*r1**2
    T2 = 1.0/r2 + 0.5*r2**2
    # Equation 3.64 in Murray and Dermott
    U = mu1*T1 + mu2*T2 - 0.5*mu1*mu2 - Vref
    return U

def Potential2(y, *data):
    #Unpack tuple
    x, z, mu1, mu2, Vref = data
    r1 = math.sqrt((x+mu2)**2 + y**2 + z**2)
    r2 = math.sqrt((x-mu1)**2 + y**2 + z**2)
    T1 = 1.0/r1 + 0.5*r1**2
    T2 = 1.0/r2 + 0.5*r2**2
    # Equation 3.64 in Murray and Dermott
    U = mu1*T1 + mu2*T2 - 0.5*mu1*mu2 - Vref
    return U

# secondary / primary mass: M2/M1 (M1 > M2)
q = 0.2
# Number of points used in contour plot and in Roche Lobe
npts = 251

# Number of contours in contour plot
nc = 75
#Equations are from Solar System Dynamics by Murray and Dermott
# Equation 3.1
mu_bar = q / (1.0 + q)
# Equation 3.2, Location of Mass 1 (primary) is (-mu2, 0, 0)
mu1 = 1.0 - mu_bar
# Equation 3.2, Location of Mass 2 (secondary) is (mu1, 0, 0)
mu2 = mu_bar

#Define the Lagrangian Points
ratio = mu2 / mu1
alpha = (ratio/3.0)**(1.0/3.0) # Equation 3.75
L1_r2 = alpha - alpha**2/3.0 - alpha**3/9.0 - 23.0*alpha**4/81.0
L1_y = 0.0 # Equation 3.83
L2_r2 = alpha + alpha**2/3.0 - alpha**3/9.0 - 31.0*alpha**4/81.0
L2_y = 0.0 # Equation 3.88

# Equation 3.93
beta = -7.0*ratio/12.0 + 7.0*ratio**2/12.0 - 13223.0*ratio**3/20736.0
L3_r1 = 1.0 + beta
L3_y = 0.0 # Equation above 3.92
L4_x = 0.5 - mu2
L4_y = +sqrt(3.0)/2.0 # Equation 3.71
L5_x = 0.5 - mu2
L5_y = -sqrt(3.0)/2.0 # Equation 3.71
# L4 and L5 are done.

# Corrections to L1, L2, and L3...
L1_r2 = newton(dPotential1, L1_r2, args=(mu1,mu2))
L1_r1 = 1.0 - L1_r2 # Equation 3.72
L1_x = L1_r1 - mu2 # Equation 3.72
L2_r2 = newton(dPotential2, L2_r2, args=(mu1, mu2))
L2_r1 = 1.0 + L2_r2 # Equation 3.84
L2_x = L2_r1 - mu2 # Equation 3.84
L3_r1 = newton(dPotential3, L3_r1, args=(mu1, mu2))
L3_r2 = 1.0 + L3_r1 # Equation 3.89
L3_x = -L3_r1 - mu2 # Equation 3.89
# Now, calculate the Roche Lobe around both stars
# Potentials at L1, L2, and L3
L1_U = Potential(L1_x, 0.0, 0.0, mu1, mu2, 0.0)
L2_U = Potential(L2_x, 0.0, 0.0, mu1, mu2, 0.0)
L3_U = Potential(L3_x, 0.0, 0.0, mu1, mu2, 0.0)

# Find x limits of the Roche Lobe
L1_left = newton(Potential, L3_x, args=(0.0, 0.0, mu1, mu2, L1_U))
L1_right = newton(Potential, L2_x, args=(0.0, 0.0, mu1, mu2, L1_U))
xx = np.linspace(L1_left, L1_right, npts)
zz = np.linspace(0.0,0.0, npts)
yc = np.linspace(0.0,0.0, npts)
for n in range(1,npts-1):
    try:
        yguess = newton(Potential2, L4_y/10.0, \
            args=(xx[n], zz[n], mu1, mu2, L1_U), maxiter = 10000)
    except:
        yguess = 0.0
    if (yguess < 0.0): yguess = -yguess
    if (yguess > L4_y): yguess = 0.0
    yc[n] = yguess
yc[1] = 0.0
yc[npts-1] = 0.0
