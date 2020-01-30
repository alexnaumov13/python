import numpy as np
import sympy as sym
x = [2, 6, 7, 8, 9, 10, 11, 13, 14, 15]
y = [-2, 2, 3, 4, 5, 6, 7, 7, 6, 5]
eps = 0.002
y0 = 0
def factorial(n):
    P = 1
    for i in range (1, n + 1):
        P = P*i
    return(P)
for i in range(len(x)):
    if y[i] < y0:
        y[i] = x[i+1]
    else: break
y = [-2, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5]
XX = [x[i], x[i-1], x[i+1], x[i+2], x[i+3], x[i+4], x[i+5], x[i+6], x[i+7],x[i+8]]#,x[i-2], x[i+2], x[i-3], x[i+3], x[i-4], x[i+4],x[i-5],x[i+5], x[i-6], x[i+6], x[i-7]]#, x[i+7], x[i+8]]
YY = [y[i], y[i-1], y[i+1], y[i+2], y[i+3], y[i+4], y[i+5], y[i+6], y[i+7], y[i+8]]#,y[i-2], y[i+2], y[i-3], y[i+3], y[i-4], y[i+4], y[i-5],y[i+5],y[i-6],y[i+6], y[i-7]]#, y[i+7], y[i+8]]
print(XX)
print(YY)
razd_el = np.zeros(([len(XX), len(XX)]))
for k in range(len(YY)):
    razd_el[k, 0] = XX[k]
for i in range(1, len(XX)):
    for j in range(0, len(XX)-i):
        razd_el[j, i] = (razd_el[j+1, i-1]-razd_el[j, i-1])/(YY[i+j]-YY[j])
# print(razd_el)
mn = razd_el[0, 0]
p = 1
for i in range(1, len(XX)):
    if abs(p*(y0-YY[i-1])*(razd_el[0, i])/factorial(i)) > eps:
        p = p*(y0-YY[i-1])/factorial(i)
        mn = mn+p*(razd_el[0, i])
        print('Погрешность на ', i, 'итеррации равна:', abs(p * (y0 - YY[i - 1]) * (razd_el[0, i]) / factorial(i - 1)))
        # print(razd_el[0,i])
    else: break
print('Значение в точке', y0, '=', mn)