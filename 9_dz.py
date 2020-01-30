import math
import numpy as np
import matplotlib.pyplot as plt
import random

def priamii_iter(a,N, eps):
    E = 13
    h = a / N
    print(h)
    A = np.zeros([N + 1, N + 1])
    B = np.zeros(N + 1)
    X = np.zeros(N + 1)
    E_new = np.zeros(100)
    E_new[0] = E
    it = 1

    for i in range(N + 1):
        B[i] = random.randint(0, 100)

    # #Р·Р°РїРѕР»РЅРµРЅРёРµ РјР°С‚СЂРёС†С‹ СЃ Р·Р°РЅСѓР»РµРЅРёРµРј 0-РіРѕ Рё N СЌР»РµРјРµРЅС‚Р°
    for n in range(1, N):
        A[n][n] = - 2 / h ** 2
        A[n][n + 1] = 1 / h ** 2 + 2 / h
        A[n][n - 1] = 1 / h ** 2 - 2 / h
    A[1][0] = 0
    A[N - 1][N] = 0
    print("Р—Р°РїРѕР»РЅРµРЅРЅР°СЏ РјР°С‚СЂРёС†Р° Рђ\n", A)
    print()

    # РјРµС‚РѕРґ РїСЂРѕРіРѕРЅРєРё
    ksi = np.zeros(N + 1)
    eta = np.zeros(N + 1)
    ksi[2] = A[1][2] / A[1][1]
    eta[2] = -B[1] / A[1][1]
    for n in range(2, N):
        ksi[n + 1] = A[n][n + 1] / (A[n][n] - A[n][n - 1] * ksi[n])
        eta[n + 1] = (A[n][n - 1] * eta[n] - B[n]) / (A[n][n] - A[n][n - 1] * ksi[n])
        print(ksi[n + 1], "\t", eta[n + 1], "\n")
    ksi[N] = 0
    eta[N] = (A[N - 1][N - 2] * eta[N - 1] - B[N - 1]) / (A[N - 1][N - 1] - A[N - 1][N - 2] * ksi[N - 1])

    k = N - 1
    while k != -1:
        X[k] = ksi[k + 1] * X[k + 1] + eta[k + 1]
        # print(k,"\t", X[k],"\n")
        k -= 1
    print("Р’РµРєС‚РѕСЂ X(СЃРѕР±СЃС‚РІРµРЅРЅС‹Рµ С„СѓРЅРєС†РёРё)\n", X)
    print()

    E_new[it] = np.inner(X, X) / np.inner(B, X)
    X = X / np.linalg.norm(X, ord=2)

    while (abs((E_new[it - 1] - E_new[it]) / (E_new[it - 1] + E_new[it])) > eps):
        print("РќРѕРјРµСЂ РёС‚РµСЂР°С†РёРё: ", it, ", cРѕР±СЃС‚РІРµРЅРЅРѕРµ Р·РЅР°С‡РµРЅРёРµ:", E_new[it])
        for n in range(N + 1):
            B[n] = X[n]

        ksi[2] = A[1][2] / A[1][1]
        eta[2] = -B[1] / A[1][1]
        for n in range(2, N):
            ksi[n + 1] = A[n][n + 1] / (A[n][n] - A[n][n - 1] * ksi[n])
            eta[n + 1] = (A[n][n - 1] * eta[n] - B[n]) / (A[n][n] - A[n][n - 1] * ksi[n])
            # print(ksi[n + 1], "\t", eta[n + 1], "\n")
        ksi[N] = 0
        eta[N] = (A[N - 1][N - 2] * eta[N - 1] - B[N - 1]) / (A[N - 1][N - 1] - A[N - 1][N - 2] * ksi[N - 1])
        k = N - 1
        while k != -1:
            X[k] = ksi[k + 1] * X[k + 1] + eta[k + 1]
            k -= 1

        it += 1
        E_new[it] = np.inner(X, X) / np.inner(B, X)
        X = X / np.linalg.norm(X, ord=2)
        plt.plot(X)
        plt.grid(True)
        plt.show()

def obratnii_iter(a, N, eps):
    E = 13
    h = a/N
    print (h)
    A = np.zeros([N+1,N+1])
    B = np.zeros(N + 1)
    X = np.zeros(N + 1)
    E_new = np.zeros(100)
    E_new[0] = E
    it = 1

    for i in range(N+1):
        B[i] = random.randint(0,100)

    # #Р·Р°РїРѕР»РЅРµРЅРёРµ РјР°С‚СЂРёС†С‹ СЃ Р·Р°РЅСѓР»РµРЅРёРµРј 0-РіРѕ Рё N СЌР»РµРјРµРЅС‚Р°
    for n in range(1,N):
        A[n][n] = - 2/h**2 + E
        A[n][n+1] = 1/h**2 + 2/h
        A[n][n-1] = 1/h**2 - 2/h
    A[1][0] = 0
    A[N-1][N] = 0
    print("Р—Р°РїРѕР»РЅРµРЅРЅР°СЏ РјР°С‚СЂРёС†Р° Рђ\n", A)
    print()

    #РјРµС‚РѕРґ РїСЂРѕРіРѕРЅРєРё
    ksi = np.zeros(N+1)
    eta = np.zeros(N+1)
    ksi[2] = A[1][2]/A[1][1]
    eta[2] = -B[1]/A[1][1]
    for n in range(2,N):
        ksi[n+1] = A[n][n+1]/(A[n][n] - A[n][n-1]*ksi[n])
        eta[n+1] = (A[n][n-1] * eta[n] - B[n])/(A[n][n] - A[n][n-1]*ksi[n])
        print(ksi[n+1],"\t", eta[n+1],"\n")
    ksi[N] = 0
    eta[N] = (A[N-1][N-2] * eta[N-1] - B[N-1])/(A[N-1][N-1] - A[N-1][N-2]*ksi[N-1])

    k = N-1
    while k != -1:
        X[k] = ksi[k+1]*X[k+1] + eta[k+1]
        #print(k,"\t", X[k],"\n")
        k -= 1
    print("Р’РµРєС‚РѕСЂ X(СЃРѕР±СЃС‚РІРµРЅРЅС‹Рµ С„СѓРЅРєС†РёРё)\n", X)
    print()

    E_new[it] = E + np.inner(X,B)/np.inner(X,X)
    X = X / np.linalg.norm(X, ord=2)

    while (abs((E_new[it - 1] - E_new[it]) / (E_new[it - 1] + E_new[it])) > eps):
        print("РќРѕРјРµСЂ РёС‚РµСЂР°С†РёРё: ",it,", cРѕР±СЃС‚РІРµРЅРЅРѕРµ Р·РЅР°С‡РµРЅРёРµ:", E_new[it])
        for n in range (N+1):
            B[n] = X[n]

        for n in range(1, N):
            A[n][n] = - 2 / h ** 2 + E_new[it]
            A[n][n + 1] = 1 / h ** 2 + 2 / h
            A[n][n - 1] = 1 / h ** 2 - 2 / h
        A[1][0] = 0
        A[N - 1][N] = 0

        ksi[2] = A[1][2] / A[1][1]
        eta[2] = -B[1] / A[1][1]
        for n in range(2, N):
            ksi[n + 1] = A[n][n + 1] / (A[n][n] - A[n][n - 1] * ksi[n])
            eta[n + 1] = (A[n][n - 1] * eta[n] - B[n]) / (A[n][n] - A[n][n - 1] * ksi[n])
            #print(ksi[n + 1], "\t", eta[n + 1], "\n")
        ksi[N] = 0
        eta[N] = (A[N - 1][N - 2] * eta[N - 1] - B[N - 1]) / (A[N - 1][N - 1] - A[N - 1][N - 2] * ksi[N - 1])
        k = N - 1
        while k != -1:
            X[k] = ksi[k + 1] * X[k + 1] + eta[k + 1]
            k -= 1

        it+=1
        E_new[it] = E_new[it-1] + np.inner(X, B) / np.inner(X, X)
        X = X / np.linalg.norm(X, ord=2)
    # plt.plot(X)
    # plt.grid(True)
    # plt.show()

priamii_iter(1, 40, 1e-4)