
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# заметка: перегрузить все математические операторы.


style.use('bmh')
#задаем параметры среды
eps_0=1
eps_1 = 1.52 #диэлектрическая проницаемость
c = (3*(10**8))/(eps_1) #скорость света в среде. Потом заменить значения
g = 0.03
lymbda = 50*(10**(-9)) #длина падающей волны
h = 150*(10**(-9))
k = (2*math.pi)/(lymbda)
w = k*c
O = math.pi/4
E1=1
E3=1

angle = 0.1
while angle<=90:

    teta = math.radians(angle)
    kx = k*math.cos(teta)


    x = kx*c/w

# делаем все для q
    q = np.zeros((1,4))

    q[0,0] = (w/c)*math.sqrt(eps_1-x**2+(g/eps_1)*math.sqrt(eps_1*(eps_1 - x**2)))
    q[0,1] = -(w/c)*math.sqrt(eps_1-x**2+(g/eps_1)*math.sqrt(eps_1*(eps_1 - x**2)))
    q[0,2] = (w/c)*math.sqrt(eps_1-x**2-(g/eps_1)*math.sqrt(eps_1*(eps_1 - x**2)))
    q[0,3] = -(w/c)*math.sqrt(eps_1-x**2-(g/eps_1)*math.sqrt(eps_1*(eps_1 - x**2)))

# делаем все для Fi
    Fi = np.zeros((4,4), dtype=np.complex)

    Fi[0,0] = 1
    Fi[0,1] = 1
    Fi[0,2] = 1
    Fi[0,3] = 1

    Fi[1,0] = c*q[0,0]/w
    Fi[1,1] = c*q[0,1]/w
    Fi[1,2] = c*q[0,2]/w
    Fi[1,3] = c*q[0,3]/w

    Fi[2,0] = 1j*(math.sqrt((eps_1-x**2)/eps_1))
    Fi[2,1] = 1j*(math.sqrt((eps_1-x**2)/eps_1))
    Fi[2,2] = -1j*(math.sqrt((eps_1-x**2)/eps_1))
    Fi[2,3] = -1j*(math.sqrt((eps_1-x**2)/eps_1))

    Fi[3,0] = (1j*q[0,0]*c/w)*math.sqrt(eps_1/(eps_1-x**2))
    Fi[3,1] = (1j*q[0,1]*c/w)*math.sqrt(eps_1/(eps_1-x**2))
    Fi[3,2] = -(1j*q[0,2]*c/w)*math.sqrt(eps_1/(eps_1-x**2))
    Fi[3,3] = -(1j*q[0,3]*c/w)*math.sqrt(eps_1/(eps_1-x**2))

# делаем обратную ей матрицу

    Fi_inv = np.linalg.inv(Fi)

# делаем все delta
    delta = np.zeros((4,4), dtype=np.complex)

    delta[0,1] = 1 - (x**2)/eps_1
    delta[1,0] = eps_1
    delta[1,2] = -1j*g
    delta[2,3] = 1
    delta[3,0] = 1j*g
    delta[3,3] = eps_1 - x**2

# делаем всю историю для P1
    P1 = np.zeros((4,4), dtype=np.complex)

    P1[0,0] = (math.sqrt((eps_1-x**2)/eps_1))
    P1[0,1] = (math.sqrt((eps_1-x**2)/eps_1))
    P1[1,0] = math.sqrt(eps_1)
    P1[1,1] = -math.sqrt(eps_1)
    P1[2,2] = 1
    P1[2,3] = 1
    P1[3,2] = math.sqrt(eps_1-x**2)
    P1[3,3] = -math.sqrt(eps_1-x**2)

# делаем обратную P1

    P1_inv = np.linalg.inv(P1)

# делаем P2

    P2 = np.zeros((4,4), dtype=np.complex)

    P2[0,0] = math.sqrt((eps_0-x**2)/eps_0)
    P2[0,1] = math.sqrt((eps_0-x**2)/eps_0)
    P2[1,0] = math.sqrt(eps_0)
    P2[1,1] = -math.sqrt(eps_0)
    P2[2,2] = 1
    P2[2,3] = 1
    P2[3,2] = math.sqrt(eps_0-x**2)
    P2[3,3] = -math.sqrt(eps_0-x**2)

# делаем обратную Р2

    P2_inv = np.linalg.inv(P2)

# делаем все для K и создание матрицы P

    K0 = np.zeros((4,4), dtype=np.complex)
    K0[0,0] = cmath.exp(1j*q[0,0]*h)
    K0[1,1] = cmath.exp(1j*q[0,1]*h)
    K0[2,2] = cmath.exp(1j*q[0,2]*h)
    K0[3,3] = cmath.exp(1j*q[0,3]*h)


    P_ = np.dot(Fi, K0)
    P = np.dot(P_, Fi_inv)

# Делаю матрицу T

    T_ = np.dot(P2_inv, P)
    T = np.dot(T_, P1)

    D = d = T[1,1]*T[3,3] - T[1,3]*T[3,1]

# делаем матрицу r

    r = np.zeros((4,4), dtype=np.complex)

    r[1,0] = (T[1,3]*T[3,0] - T[1,0]*T[3,3])/D
    r[3,0] = (T[1,0]*T[3,1] - T[1,1]*T[3,0])/D
    r[1,2] = (T[1,3]*T[3,2] - T[1,2]*T[3,3])/D
    r[3,2] = (T[1,2]*T[3,1] - T[1,1]*T[3,2])/D

# выражение R

    R = ((r[1,0])*np.conjugate(r[1,0]) + (r[3,0])*np.conjugate(r[3,0]))/2 + ((r[1,2])*np.conjugate(r[1,2]) + (r[3,2])*np.conjugate(r[3,2]))/2


    # print("Matrix of q's\n", q)
    # print("Matrix of Fi's\n", Fi)
    # print("Matrix of Fi_inv's\n", Fi_inv)
    # print("Matrix of delta's\n", delta)
    # print("Matrix of P1's\n", P1)
    # print("Matrix of P2's\n", P2)
    print (R)
    plt.scatter(angle, R, marker='D', s=3, color='blue')

    angle += 1


plt.show()