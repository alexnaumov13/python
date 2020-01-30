import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
X = [ 1, 2, 3, 4, 5, 6]
U0 = [ 1, 0.5, 0.33333, 0.25, 0.2, 0.16666667]
U =[]
U.append(U0)
N = len(X)
i = 1
while i < N:
    U.append([])
    n = 0
    while n < (N - i):
        U[i].append((U[i-1][n] - U[i-1][n+1])/(X[n] - X[n+i]) * i)
        n += 1
    i += 1
print(U)
def inter(x):
    S = 0
    n = 0
    while n < N:
        k = 0
        P = 1
        while k <= (n - 1):
            P *= (x - X[k])
            k += 1
        S += (U[n][0] / math.factorial(n)) * P
        n += 1
    return S

x = symbols('x')
print(inter(1.1))
x = np.linspace(0, 10, 1000)
plt.figure()
plt.xlabel("x")
plt.ylabel("y(x)")
plt.plot(x, inter(x))
plt.scatter(X, U0, color = 'black')
plt.show()