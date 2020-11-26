
# 
# Functions from https://www.sfu.ca/~ssurjano/optimization.html

import numpy as np
import math


def ackley(args):
    # """Ackley function

    # Global minimum: f(0,0) = 0.0
    # Search domain: -5.0 <= x, y <= 5.0
    # """
    first_sum = 0.0
    second_sum = 0.0
    for c in args:
        first_sum += c ** 2.0
        second_sum += np.cos(2.0 * np.pi * c)
    n = float(len(args))
    return -20.0*np.exp(-0.2*np.sqrt(first_sum/n)) - np.exp(second_sum/n) + 20.0 + np.e

def bukin6(args):
    x1,x2 = args
    term1 = 100 * np.sqrt(abs(x2 - 0.01*x1**2))
    term2 = 0.01 * abs(x1+10)
    
    y = term1 + term2;
    return y

def crossit(args):
    
    x1,x2 = args
    fact1 = np.sin(x1)*np.sin(x2)
    fact2 = np.exp(abs(100 - np.sqrt(x1**2+x2**2)/np.pi))
    
    y = -0.0001 * (abs(fact1*fact2)+1)**0.1
    
    return y

def drop(args):
    x1,x2 = args
    
    frac1 = 1 + np.cos(12*np.sqrt(x1**2+x2**2))
    frac2 = 0.5*(x1**2+x2**2) + 2
    
    y = -frac1/frac2
    return y

def egg(args):
    x1,x2 = args
     
    term1 = -(x2+47) * np.sin(np.sqrt(abs(x2+x1/2+47)))
    term2 = -x1 * np.sin(np.sqrt(abs(x1-(x2+47))))
     
    y = term1 + term2
    return y

a = np.array([0.1, 0.1])
print(egg(a))