import numpy as np
import math as m

a = 1
b = 9
N = int(input())
K = int(input())
p = 2
integ = np.eye(K)
runge = np.eye(K - 1)
peff = np.eye(K - 2)
r = 2


def f(x):
    return 1 / (x ** 0.5)


for j in range(K):
    sum = 0
    xi = a
    h = (b - a) / N
    for i in range(N):
        sum = sum + (f(xi) + f(xi + h)) * h / 2
        xi = xi + h
    N = r * N
    integ[j, 0] = sum
q = 0
for i in range(1, K):
    for j in range(i, K):
        R = (integ[j, i - 1] - integ[j - 1, i - 1]) / (r ** (p + q) - 1)
        runge[j - 1, i - 1] = R
        integ[j, i] = integ[j, i - 1] + runge[j - 1, i - 1]
        # peff[j-1, i-1] = m.log2(abs((runge[j-1, i-1])/(runge[j,i-1])))

    q = q + 2
for i in range(2, K):
    for j in range(i, K):
        peff[j - 2, i - 2] = m.log2(abs((runge[j - 2, i - 2]) / (runge[j - 1, i - 2])))
print(integ)
print(runge)
# for i in range(K-2):
# print(peff[i, 1])
print(peff)