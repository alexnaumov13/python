import math as m
import numpy as np
#import numpy as np
#import pandas as pd
import sympy as sym


x = sym.Symbol('x')


f = 1/(x**(0.5))  #sym.Symbol(input("Введите функцию: "))  #1/(1+x**2)
f = sym.lambdify(x, f, 'numpy')



def integral_trap(a, b, N):
    sum = 0
    xi = a
    h = (b - a) / N
    for i in range(N):
        sum = sum + (f(xi) + f(xi + h)) * h / 2
        xi = xi + h
    return sum

def solve_richardson():
    r = 2  # сгущение сетки
    w = 7  # кол-во строк
    p = 2  # порядок точности
    N = 1  # int(input('Введите число интервалов: '))
    a = 1  # int(input('Введите начало отрезка: '))
    b = 9  # int(input('Введите конец отрезка: '))

    U = np.zeros((w,w))
    R0 = np.zeros((w, w))
    P_eff = np.zeros((w, w))

    # заполняем матрицу начальными элементами, для последующей реализации цикла
    N_new = N
    for j in range(w):
        U[j][0] = integral_trap(a,b, N_new)
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
        q = q + 2

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
                print("N = ", '{:<4d}'.format(2 ** (i+1)), '{:8.5f}'.format(R0[i][j]), end='    ')
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