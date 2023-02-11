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
