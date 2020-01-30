import math
import numpy as np
#import numpy as np
#import pandas as pd

def f(x):
    return 1/(1+x**2)

def integ(a, b, N):
    h = (b - a) / N
    I = 0.5 * (f(a) + f(b))
    for i in range (1, N):
        I = I + (f(i*h)+f((i+1)*h))*h*0.5
    return I

def richardson(a, b, N, sgush):
    print("ЗНАЧЕНИЯ ПО РИЧАРДСОНУ:\n")
    p = 2
    r = 2
    t = 0
    U = np.zeros([6,6])
    R_new = np.zeros([6, 6])
    P_eff = np.zeros([6, 6])

    print("Начальная сетка:", N, "\n")
    N_new = N * r
    U0 = integ(a, b, N)
    U1 = integ(a, b, N_new)
    R_new[1][0] = (U1 - U0) / (r**p - 1) #погрешность на первой итерации
    U[0][0] = U0
    U[1][0] = U1
    for k in range (2, sgush+1):
        N_new *= 2
        U[k][0] = integ(a, b, N_new)
        R_new[k][0] = (U[k][0] - U[k-1][0]) / (r**p  - 1)
        P_eff[k][0] = math.log10(abs(R_new[k-1][0]/R_new[k][0]))/math.log10(r)
        k += 1
        #print(N_new)


    for j in range (1,sgush+1):
        k = j
        t = j
        while k <= sgush:
            U[k][j] = U[k][j-1] + R_new[k][j-1]
            k += 1
        while t < sgush:
            p = p + 2 * j
            R_new[t + 1][j] = (U[t][j] - U[t - 1][j]) / (r ** p - 1)
            t+=1
        t = j
        while (t < (sgush - 1)):
            P_eff[t+2][j] = math.log10(abs(R_new[t + 1][j] / R_new[t + 2][j])) / math.log10(r)
            t+=1

    N_new = N
    print("Значения интеграла:\n")
    for j in range (sgush+1):
        print (" N = ", N_new, end = '    ')
        N_new *= 2
    print()
    for j in range (sgush+1):
        for k in range (j+1):
            print('{:8.5f}'.format(U[j][k]), end = '   ')
        print()
    print("\n")

    N_new = N*r
    print("Значение ошибок:\n")
    for j in range (sgush):
        #print("N = ", N_new, end="   ")
        for k in range (j+1):
            print('{:8.7f}'.format(R_new[j+1][k]), end='   ')
        N_new*=2
        print()
    print("\n")

    N_new = N*r*r
    print("Значение P_eff:\n")
    for j in range(sgush-1):
        #print("N = ", N_new, end="   ")
        for k in range(j + 1):
            print('{:8.9f}'.format(R_new[j + +2][k]), end='   ')
        N_new*=2
        print()
    print("\n")
    return U

richardson(-1, 1, 1, 5)

# a = 0
# b = 10
# N = 1
# r = 2
# error = 0.1
# p_0 = 2
# q = 2
#
# n = 0
# x = []
# R = []
# p_eff = []
# while n < 5:
#     x.append([])
#     R.append([])
#     p_eff.append([])
#     if n == 0:
#         m = 3
#         x[n].append(tr(a, b, N))
#         x[n].append(tr(a, b, r * N))
#         x[n].append(tr(a, b, r*r * N))
#         R[n].append(0)
#         R[n].append((x[n][1] - x[n][0]) / (r * (p_0 + q * n) - 1))
#         R[n].append((x[n][2] - x[n][1]) / (r * (p_0 + q * n) - 1))
#         p_eff[n].append(0)
#         p_eff[n].append(0)
#         p_eff[n].append(abs(math.log2(abs(R[n][2] / R[n][1]))))
#         while m < 10:
#             x[n].append(tr(a, b, pow(r, m) * N))
#             R[n].append((x[n][m] - x[n][m-1]) / (r * p_0  - 1))
#             p_eff[n].append(abs(math.log2(abs(R[n][m] / R[n][m-1]))))
#             m += 1
#         n += 1
#     else:
#         m = 0
#         while m < 10:
#             if m < n:
#                 x[n].append(0)
#             else:
#                 x[n].append(x[n-1][m] + R[n-1][m])
#             if m < n + 1:
#                 R[n].append(0)
#             else:
#                 R[n].append((x[n][m] - x[n][m-1]) / (r * (p_0 + q * n) - 1))
#             if m < n + 2:
#                 p_eff[n].append(0)
#             else:
#                 p_eff[n].append(abs(math.log2(abs(R[n][m] / R[n][m-1]))))
#             m += 1
#         n += 1
# print("x:\n",x)
# print("R:\n",R)
# print("p_eff\n",p_eff)