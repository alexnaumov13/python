import numpy as np
import math as m
import matplotlib.pyplot as plt

dx = 1e-2
eps = 1e-2


def input_data(N):
    X = np.array([1. for i in range(N + 1)])
    Y = np.array([1. for i in range(N + 1)])

    for i in range(N + 1):
        X[i] = float(input('Введите значения x: '.format(i)))
        Y[i] = float(input('Введите значения y: '.format(i)))

    return X, Y


def u_nk(X, Y):
    N = len(X) - 1
    u = [[1 for j in range(N - i + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        u[i][0] = Y[i]

    for k in range(1, N + 1):
        for n in range(N - k + 1):
            u[n][k] = k * (u[n][k - 1] - u[n + 1][k - 1]) / (
                    X[n] - X[n + k])

    return u


def f(x, X, Y):
    N = len(X) - 1
    arg = (np.abs(X - x)).argsort()
    X, Y = X[arg], Y[arg]
    u = u_nk(X, Y)

    result = u[0][0]

    n = 1
    add = eps + 10
    add_old = 2 * add
    P = 1
    factorial = 1
    while n <= N and abs(add) >= eps and abs(add) <= abs(add_old):
        add_old = add

        P *= (x - X[n - 1])
        add = u[0][n] * P / factorial
        result += add

        n += 1
        factorial *= n
    print(add)
    return result


def plot_f(X, Y):
    xlist = np.arange(min(X), max(X) + dx, dx)
    ylist = np.array([f(xlist[i], X, Y) for i in range(len(xlist))])

    plt.plot(xlist, ylist, X, Y, 'o')


# N + 1 - С‡РёСЃР»Рѕ С‚РѕС‡РµРє, С‚Р°Рє РєР°Рє РЅСѓРјРµСЂР°С†РёСЏ СЃ 0 РґРѕ N РІРєР»СЋС‡РёС‚РµР»СЊРЅРѕ
# N = int(input('Р’РІРµРґРёС‚Рµ N, N + 1 - С‡РёСЃР»Рѕ С‚РѕС‡РµРє: '))

# X, Y = input_data(N)
# plot_f(X, Y)
X = np.arange(0, 15, 2)
Y = np.sin(X)
# Y[8] += 0.1
# # print(f(3.7, X, Y))
# plot_f(X, Y)
# plt.show()
print(f(7,X,Y))