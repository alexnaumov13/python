#программа выполняет аппроксимацию точек с помощью базиса с фиксированным количеством базисных функций

# аппроксимация заданного набора точек по заданной системе базисных функций
import numpy as np
import sympy as sym
import math
import matplotlib.pyplot as plt

x, y = sym.symbols('x y')
a = -1
b = 1
l = (b - a) / 2


# экспонента, парабола, гауссиан - Л, синус - Т
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
    if ((m+k)%2 == 0):
        return 2/(m+k+1)
    else:
        return 0


def Scalar_multiply(x, u, v):  # численное интегрирование методом трапеций
    def rho(x):  # вес, с которым ортогональны базисные функции
        return 1

    N = len(x)
    I = 0
    for n in range(1, N):
        h = x[n] - x[n - 1]  # учитываем возможность неравномерного шага
        I += (u[n - 1] * v[n - 1] * rho(x[0] + (n - 1) * h) + u[n] * v[n] * rho(x[0] + n * h)) * h / 2
    return I



# задаем точки по х и у
# 30 точек = экспонента + рандомный разброс
N = 30
xn = np.zeros(N)
yn = np.zeros(N)#задаваемые значения
for n in range(N):
    xn[n] = a + n * (b - a) / N
    yn[n] = np.cos(-xn[n]) + np.random.uniform(-0.2, 0.2)


# аппроксимация с погрешностью
Pn = phi_n(x, 0)
Pn_n = [Pn.subs(x, xn[i]) for i in range(N)]#подставляем в функцию Pn на место x значения xn[i]
c = Scalar_multiply(xn, yn, Pn_n) / Scalar_multiply(xn, Pn_n, Pn_n)
y = c * Pn
ynn = np.zeros(N)


# матрица ошибок
delty = np.zeros(N)
for n in range(N):
    ynn[n] = y.subs(x, xn[n])#подставляем в функцию y на место x значения xn[n]
    delty[n] = 0.15


m = 1
while np.sum((ynn[:] - yn[:]) ** 2) >= np.sum(delty[:] ** 2):
    Pn = phi_n(x, m)
    Pn_n = [Pn.subs(x, xn[i]) for i in range(N)]
    c = Scalar_multiply(xn, yn, Pn_n) / Scalar_multiply(xn, Pn_n, Pn_n)
    y += c * Pn
    m += 1
    for n in range(N):
        ynn[n] = y.subs(x, xn[n])


# построение графиков
xx = np.linspace(a, b, 100)
yy = np.zeros(100)
for i in range(100):
    yy[i] = y.subs(x, xx[i])
plt.plot(xx, yy)
plt.plot(xn, yn, "ro")


plt.show()
