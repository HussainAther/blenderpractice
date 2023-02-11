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
