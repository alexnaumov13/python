import sympy as sym
import math as mt
def f(x):
    return mt.e**x-2
def df(x):
    q = sym.Symbol('x')
    df = sym.diff(f(q), q)
    return float(df.subs(q, x))
def method(n):
    eps = 0.1
    xn0 = 0
    xn = n
    xn1 = xn - f(xn)/df(xn)
    q = 1
    while abs((xn1-xn)/(1 - ((xn1 - xn) / (xn - xn0)))) > eps:
        xn0 = xn
        xn = xn1
        xn1 = xn - f(xn)/df(xn)
        q += 1
    return print('x = ', xn1), print('p = ', 1/(1 - (xn1-xn)/(xn-xn0))), print('q = ', q)
method(-2)
