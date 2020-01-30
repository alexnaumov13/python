import numpy as np

def Matrix_A(N):
    h = 1 / N
    A = np.zeros((N, N))
    for n in range(N - 1):
        A[n][n] = -2 / h ** 2
        A[n + 1][n] = 1 / h ** 2 - 2 / h
        A[n][n + 1] = 1 / h ** 2 + 2 / h
    A[N - 1][N - 1] = -2 / h ** 2
    return A

def Scalar_multiply(x, y):
    return np.sum(x[:] * y[:])

def Inverse_iteration(A):
    x0 = [1] + (len(A[0]) - 1) * [0]
    AA = np.linalg.inv(A)
    x1 = AA.dot(x0)
    for s in range(10):
        x0 = x1
        x1 = AA.dot(x0)
    l = Scalar_multiply(x0, x1) / Scalar_multiply(x1, x1)
    return l