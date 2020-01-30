import matplotlib.pyplot as plt
import numpy as np
import numpy
from sympy import diff, symbols, lambdify

x = symbols('x')

# from numpy import *

x = [0, 1, 2, 3, 4]
y = [8, 6, 3, -1, -5]

def coef(x,y) :




    # x.astype(float)
    # y.astype(float)
    n = len(x)
    F = np.zeros((n,n), dtype=float)
    b = np.zeros(n)
    for i in range(0,n):
        F[i,0]=y[i]



    for j in range(1, n):
        for i in range(j,n):
            F[i,j] = float(F[i,j-1]-F[i-1,j-1])/float(x[i]-x[i-j])

    print(F,'\n')

    for i in range(0,n):
        b[i] = F[i,i]

    print(b)

    return np.array(b) # return an array of coefficient

coef(x,y)