import math
import matplotlib.pyplot as plt
import numpy as np

#заводим константы


# правый конец
r = 1

# левый конец
l = 0

c = -0.25
t = 0.1
N = 30

# считаю и вывожу константные выражения из формул

h = (r-l)/(N-1)
A_ij1 = c * t / h
A_ij = -(1 - A_ij1)

print ("значения по главной диагонали матрицы а", A_ij)
print ("значения по побочной диагонали матрицы а", A_ij1,"\n\n")

# создаю массивы
# i - номер строки; j - номер столбца



# матрица b
b = np.zeros((N,1))
for i in range (1,N):
        b[i] = math.sin(math.pi * ((l + h*(i - 1))/(r - l)))
print ("\n матрица b:\n",b,"\n")


# матрица а
a = np.zeros((N,N))
i,j = np.indices(a.shape)
a[i==j] = A_ij
a[i==j+1] = A_ij1


# вычисляем обратную матрицу
a_inv = np.linalg.inv(a)

# матрица значений по х
step = np.zeros((N, 1))
for i in range(N):
    step[i] = (i)/N

print("матрица значений по х\n",step,"\n")

# X = np.dot(a_inv, b)
#
# print("\n X1 = ",X,"\n")


iter = 0
while iter <= N:

    # вычисляю x
    # X = np.dot(a_inv, b)
    # for n in range(1,N):
    #     X = abs((a[n][n - 1] * X[n - 1][0] - a[n][0]) / a[n][n])
    eta = np.zeros((N, 1))
    # print("X = ", X, "\n")
    for n in range(1, N):
        eta[n] = (a[n][n - 1] * eta[n - 1] - b[n][0]) / a[n][n]


    plt.plot(step,b)

    print("матрица значений по у (b):\n", b, "\n")

    b = eta

    iter += 1

plt.show()

