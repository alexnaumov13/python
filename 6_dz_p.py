import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
def f(x):
    return x*x*x
X0 = [1, 2, 3, 4, 5, 6]
U0 = []
for i in range(0, len(X0)):
    U0.append(f(X0[i]))

def inter(x):
    for k in range (0, len(X0)):
        X = []
        U = []
        for ml in range(0, k + 1):
            X.append(X0[ml])
        U.append(U0[0 : k + 1])
        #print(X, U)
        i = 1
        N = len(X)
        #print(N)
        while i < len(X) :
            U.append([])
            n = 0
            while n < (N - i):
                U[i].append((U[i - 1][n] - U[i - 1][n + 1])/(X[n] - X[n + i]) * i)
                n += 1
            i += 1
        #print(U)
        S = 0
        n1 = 0
        while n1 < N:
            P = 1
            k1 = 0
            while k1 <= (n1 - 1):
                P *= (x - X[k1])
                k1 += 1
            S += (U[n1][0] /  math.factorial(n1)) * P
            n1 += 1
        print(S)
    return S
print(inter(1.5))
'''print(len(X0))
print(X0[5])    '''
