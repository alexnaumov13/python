#программа численно считает производную в точке


import math as m
import numpy as np
#import numpy as np
#import pandas as pd
import sympy as sym


x = sym.Symbol('x')


# f = x**3  #sym.Symbol(input("Введите функцию: "))  #1/(1+x**2)
# f = sym.lambdify(x, f, 'numpy')

def f(x):
    check = x**3
    return x**3

def diff(x,h, N):
    h_new = h/N
    differential = (f(x) - f(x-h_new))/h_new
    return differential

def solve_richardson():
    p = 1
    r = 2  # сгущение сетки
    w = 7  # кол-во строк
    h1 = 1
    x_0 = 1
    N = 1

    U = np.zeros((w,w))
    R0 = np.zeros((w, w))
    P_eff = np.zeros((w, w))

    # заполняем матрицу начальными элементами, для последующей реализации цикла
    N_new = N
    for j in range(w):
        U[j][0] = diff(x_0, h1, N_new)
        N_new *= r

    # for j in range(1,w):
    #     R[i][0] = (U[i][0] - U[i - 1][0]) / (r ** p - 1)
    #
    # for i in range(2,w):
    #     P_eff[i][0] = m.log10(abs(R[i - 1][0] / R[i][0])) / m.log10(r)

    q = 0
    for i in range(1, w):
        for j in range(i, w):
            R = (U[j, i - 1] - U[j - 1, i - 1]) / (r ** (p + q) - 1)
            R0[j - 1, i - 1] = R
            U[j, i] = U[j, i - 1] + R0[j - 1, i - 1]
            # peff[j-1, i-1] = m.log2(abs((runge[j-1, i-1])/(runge[j,i-1])))
        q = q + 1

    for i in range(2, w):
        for j in range(i, w):
            P_eff[j - 2, i - 2] = m.log2(abs((R0[j - 2, i - 2]) / (R0[j - 1, i - 2])))

    print('Таблица значений интеграла:')
    for i in range(w):
        for j in range(i + 1):
            if j == 0:
                print("N = ", '{:<4d}'.format(2 ** i), '{:8.5f}'.format(U[i][j]), end='    ')
            else:
                print('{:8.5f}'.format(U[i][j]), end='    ')
        print()

    print('\nТаблица погрешностей:')
    for i in range(w-1):
        for j in range(i+1):
            if j == 0:
                print("N = ", '{:<4d}'.format(2 ** (1+i)), '{:8.5f}'.format(R0[i][j]), end='    ')
            else:
                print('{:8.5f}'.format(R0[i][j]), end='    ')
        print()

    print('\nТаблица эффективных порядков точности:')
    for i in range(w-2):
        for j in range(i + 1):
            if j == 0:
                print("N = ", '{:<4d}'.format(2 ** (i+2)), '{:8.5f}'.format(P_eff[i][j]), end='    ')
            else:
                print('{:8.5f}'.format(P_eff[i][j]), end='    ')
        print()

solve_richardson()
