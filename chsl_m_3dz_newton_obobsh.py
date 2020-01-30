import sympy
import math
from sympy import diff, symbols, lambdify

# без учета четности корня

x = symbols('x')



def dx(x0):
    a = f(x0)
    b = df(x0)
    c = f(x0) / df(x0)
    x1 = x0 - f(x0) / df(x0)
    return abs(((x1 - f(x1) / df(x1)) - x1)/(1 - (((x1 - f(x1) / df(x1)) - x1)/(x1 - x0))))

def tau(x0):
    # ksi = (-1)*f(x0)/df(x0)
    x1 = x0 - (f(x0) / df(x0))
    fi0 = (f(x0))**2.
    fi1 = (f(x1))**2.
    t = (fi0 + 0.001*fi1)/(fi0 + fi1)
    return t

def newton_1(f,df,x0,eps):

    delta = dx(x0)
    timer = 0
    # ksi = (-1)*(f(x0) / df(x0))
    # x0 = x0 - (f(x0) / df(x0))
    while delta > eps:
        # x0 = x0 - (f(x0) / df(x0))
        t = tau(x0)
        x0 = x0 - (f(x0) / df(x0))
        x0 = x0 - t*(f(x0) / df(x0))
        delta = dx(x0)
        # ksi = (-1) * (f(x0) / df(x0))
        timer += 1
    print("\nкол-во итераций ",timer,"\n")
    return x0

# f1 = 2.7**(x)-2

f = ((2.71828**x)-2.)
df = diff(f, x)

f = lambdify([x], f)
df = lambdify([x], df)



x0 = newton_1(f,df,-2.0,0.01)
print('Найденный корень: ', x0)




