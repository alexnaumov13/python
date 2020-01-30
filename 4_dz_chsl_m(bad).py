import sympy as sym
import math as mt
import numpy as np
import pprint as pp


a = -1#int(input('Введите начало отрезка: '))
b = 1#int(input('Введите конец отрезка: '))
NN = 1#int(input('Введите число интервалов: '))
r = 2 #сгущение сетки
w = 8 #кол-во строк
p = 1 # порядок точности
x = sym.Symbol('x')


f = 1/(1+x**2)  #sym.Symbol(input("Введите функцию: "))  #1/(1+x**2)
f = sym.lambdify(x, f, 'numpy')

h = [None]*w
F = np.zeros((w, NN*r**w))
u = np.zeros((w, NN*r**(w-1))) #
U = [None]*w
l = [0]*(w)
R = [0]*w

UU = np.zeros((w, w)) #матрица значений интегралов
RR = np.zeros((w, w)) #значений ошибки
PP = np.zeros((w, w)) #эффективный порядок точности


# сразу считаем все значения иксов в разные массивы(h[t], F[t,i]
for t in range(w):
    h[t] = ((b - a)/(NN*r**t)) #массив разбиений
    for i in range(int((b - a)/h[t]) + 1):
        F[t, i] = f(a + i*h[t]) #двумерный массив сеточных значений для различных разбиений
    for i in range(NN*r**(w-1)):
        #if F[t, i+1] != 0:
        u[t, i] = h[t]*F[t, 1+i]#0.5*(F[t, i] + F[t, i+1])*h[t] #двумерный массив значений по формуле трапеции
    t += 1

print('массив разбиений:')
for i in range(w):
            print('{:8.5f}'.format(h[i]), end='    ')
            print()

# print('Двумерный массив сеточных значений:')
# for t in range(w):
#     for i in range(int((b-a)/h[t]+1)):
#             print('{:8.5f}'.format(F[t][i]), end='    ')
#     print()


print("u: \n", u)
print("U: \n", U)

t = 0
for i in range(w):
    u[t] = sum(u[i]) #формула трапеций. Складываем значения по строкам
    U[i] = u[t, i] #из двумерного массива в одномерный
    UU[0, i] = U[i]
    t += 1
#print('U 0= ', U)

print("U: \n", U)
print("u: \n", u)

t = 0
while t < w - 1:
    for i in range(1, w):
        R[i] = (U[i] - U[i-1])/(r**(p + t) - 1) #добавочный коэффициент
        R[t] = 0
        RR[t, i] = R[i]
    #print('R', t, '=', R)
    if t != w - 2:
        for i in range(t + 2, w): #считаем эффективный порядок точности
            if R[i] != 0:
                l[i] = (mt.log(abs(R[i - 1]/R[i]), r)) #точность
                l[t] = 0
                l[t + 1] = 0
            else:
                l[i] = 0
                l[t] = 0
                l[t + 1] = 0
            PP[t, i] = l[i]
        #print('p', t, '=', l)
    for i in range(w): #считаем матрицу значений интегралов с уточнениями
        U[i] = U[i] + R[i] # уточнение U
        U[t] = 0
        UU[t+1, i] = U[i]
    t += 1
    #print('U', t, '=', U)


# вывод таблиц и форматирование вида
print('Таблица значений интеграла:')
for i in range(w):
    for j in range(i+1):
        if j==0:
            print("N = ",'{:<4d}'.format(2**i),'{:8.5f}'.format(UU[j][i]), end='    ')
        else:
            print('{:8.5f}'.format(UU[j][i]), end='    ')
    print()


print('\nТаблица погрешностей:')
for i in range(w):
    for j in range(i):
        if j==0:
            print("N = ",'{:<4d}'.format(2**i),'{:8.5f}'.format(RR[j][i]), end='    ')
        else:
            print('{:8.5f}'.format(RR[j][i]), end='    ')
    print()

print('\nТаблица эффективных порядков точности:')
for i in range(w):
    for j in range(i-1):
        if j==0:
            print("N = ",'{:<4d}'.format(2**i),'{:8.5f}'.format(PP[j][i]), end='    ')
        else:
            print('{:8.5f}'.format(PP[j][i]), end='    ')
    print()



