#программа выполняет аппроксимацию точек с помощью базиса с фиксированным количеством базисных функций

# аппроксимация заданного набора точек по заданной системе базисных функций
import numpy as np
import sympy as sym
import math
import matplotlib.pyplot as plt

x = sym.symbols('x')
a = 0
b = 10
l = (b - a) / 100
pogr = 0.1


def phi_n(x, n):  # полиномы Лежандра
    return 1 / (2 ** n * math.factorial(n)) * sym.diff((x ** 2 - 1) ** n, x, n)

def polinomi(x, n):
    return x**n

# def trigonometric_system(x, n, parity=True):  # тригонометрическая система (не нормирована)
#     if n == 0:
#         return sym.cos(0 * x)
#     if parity == False:
#         return sym.sin(np.pi * n * x / l)
#     if parity == True:
#         return sym.cos(np.pi * n * x / l)

def Scalar_polynoms(k,m):
    # a = -10
    # b = 10
    if ((m+k)%2 == 0):
        return (b**(m+k+1) - a**(m + k + 1))/(m+k+1)
    else:
        return 0


def Scalar_multiply(xn, i,j):  # численное интегрирование методом трапеций
    def rho(x):  # вес, с которым ортогональны базисные функции
        return 1

    sum = 0
    for m in range(N):
        sum += polinomi(xn[m], i) * polinomi(xn[m], j) * ((b - a) / N)

    return sum



# задаем точки по х и у
# 30 точек = экспонента + рандомный разброс
N = 30
R = 1
xn = np.zeros(N)
yn = np.zeros(N)#задаваемые значения
ynn = np.zeros(N)



for n in range(N):
    xn[n] = a + n * (b - a) / N
    yn[n] = np.exp(xn[n]) + np.random.uniform(-0.1, 0.1)



Fi = np.zeros([R, R])
for i in range(R):
    for j in range(R):
        # Fi[i, j] = Scalar_polynoms(i, j)
        #        если несимметричные пределы или базис - не степенные полиномы используем общую формулу скалярного произведения
        Fi[i, j] = Scalar_multiply(xn, i, j)
print(Fi)

# матрица скалярных произведений U на фи
U_n = np.zeros([R, 1])
for i in range(R):
    sum = 0
    for m in range(N):
        sum += yn[m] * polinomi(xn[m], i) * ((b - a) / N)
    U_n[i, 0] = sum

# print(U_n)


# numpy.linalg.solve(левая часть системы, правая часть системы)
C = np.linalg.solve(Fi, U_n)
# print(C)
y = 0
for l in range(R):
    k = float(C[l])
    y += k * polinomi(x, l)

# матрица ошибок
delty = np.zeros(N)
for n in range(N):
    ynn[n] = y.subs(x, xn[n])
    delty[n] = pogr

R = 2 # начальное количество базисных функций
while np.sum((ynn[:] - yn[:]) ** 2) >= np.sum(delty[:] ** 2):
    # матрица скалярных произведений фи на фи
    Fi = np.zeros([R, R])
    for i in range(R):
        for j in range(R):
            # Fi[i,j] = Scalar_polynoms(i,j)
    #        если несимметричные пределы или базис - не степенные полиномы используем общую формулу скалярного произведения
            Fi[i,j] = Scalar_multiply(xn,i,j)
    print(Fi)

    # матрица скалярных произведений U на фи
    U_n = np.zeros([R,1])
    for i in range(R):
        sum = 0
        for m in range(N):
            sum += yn[m]*polinomi(xn[m],i)*((b-a)/N)
        U_n[i,0] = sum

    # print(U_n)


    # numpy.linalg.solve(левая часть системы, правая часть системы)
    C = np.linalg.solve(Fi, U_n)
    # print(C)
    y = 0
    for l in range(R):
        k = float(C[l])
        y += k*polinomi(x, l)

    # y = sym.lambdify([x], y)

    for n in range(N):
        ynn[n] = y.subs(x, xn[n])

    R += 1

y = sym.lambdify([x], y)
xx = np.linspace(a, b, 100)
yy = np.zeros(100)
for i in range(100):
    yy[i] = float(y(xx[i]))
plt.plot(xx, yy)


plt.plot(xn, yn, "ro")

for n in range(N):
    plt.errorbar(xn[n], yn[n], delty[n], marker='o', mfc='red')

plt.show()
