from sympy import diff, symbols, lambdify


x = symbols('x')

f = x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108
df = diff(f,x)

f = lambdify([x], f)
df = lambdify([x], df)

def chetnost(x0):
    x1 = x0 - f(x0) / df(x0)
    x2 = x1 - f(x1) / df(x1)
    return abs(1 / (1 - ((x2 - x1) / (x1 - x0))))


def dx(x0):
    x1 = x0 - f(x0) / df(x0)
    x2 = x1 - f(x1) / df(x1)
    return abs((x2 - x1)/(1 - ((x2 - x1)/(x1 - x0))))

def newton_2(f,df,x0,eps):
    delta = dx(x0)
    while delta > eps:
        x0 = x0 - f(x0) / df(x0)
        delta = dx(x0)
        p = chetnost(x0)
        # print("X = ", x0, "\n")
        # print("следующая итерация\n")

    return x0, p


x0,p0 = newton_2(f,df,4,0.01)
print('Найденный корень: ', x0)
print('четность корня: ', p0, "\n")



f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/((x-x0)**p0)
df = diff(f,x)
f = lambdify([x], f)
df = lambdify([x], df)



x1,p1 = newton_2(f,df,4,0.01)
print('Найденный корень: ', x1)
print('четность корня: ', p1, "\n")



f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/(((x-x0)**p0)*((x-x1)**p1))
df = diff(f,x)
f = lambdify([x], f)
df = lambdify([x], df)



x2,p2 = newton_2(f,df,4,0.01)
print('Найденный корень: ', x2)
print('четность корня: ', p2, "\n")



f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/(((x-x0)**p0)*((x-x1)**p1)*((x-x2)**p2))
df = diff(f,x)
f = lambdify([x], f)
df = lambdify([x], df)



x3,p3 = newton_2(f,df,4,0.01)
print('Найденный корень: ', x3)
print('четность корня: ', p3, "\n")


