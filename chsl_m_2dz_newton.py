import sympy
import math
from sympy import diff, symbols, lambdify

# без учета четности корня

x = symbols('x')

# def df(x):
#     return 6*x**5 - 70*x**4 + 320*x**3 - 714*x**2 + 774*x - 324

# def f(x):
#     return x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108

# f = x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)

# print(f(4))
# print(df(1))

# критерий останова
# x0 = 4
# x1 = x0 - f(x0) / df(x0)
# x2 = x1 - f(x1) / df(x1)
# print(x1)
# print(x2)
# print(abs((x2 - x1)/(1 - ((x2 - x1)/(x1 - x0)))))

def dx(x0):
    x1 = x0 - f(x0) / df(x0)
    x2 = x1 - f(x1) / df(x1)
    return abs((x2 - x1)/(1 - ((x2 - x1)/(x1 - x0))))

def newton_1(f,df,x0,eps):
    # f = lambdify([x], f)
    # df = lambdify([x], df)
    delta = dx(x0)
    while delta > eps:
        x0 = x0 - f(x0) / df(x0)
        delta = dx(x0)
        # print("X = ", x0, "\n")
        # print("следующая итерация\n")
    # print('Найденный корень: ', x0)
    # print('Значение функции в этой точке: ', f(x0))
    return x0

f1 = x ** 6 - 14 * x ** 5 + 80 * x ** 4 - 238 * x ** 3 + 387 * x ** 2 - 324 * x + 108
f = x ** 6 - 14 * x ** 5 + 80 * x ** 4 - 238 * x ** 3 + 387 * x ** 2 - 324 * x + 108
df = diff(f, x)

f = lambdify([x], f)
df = lambdify([x], df)

for i in range(6):

    x0 = newton_1(f,df,4,0.01)
    print('Найденный корень: ', x0)

    f1 = f1/(x-x0)
    print(f1)
    df1 = diff(f1, x)
    f2 = lambdify([x], f1)
    df2 = lambdify([x], df1)

    f = f2
    df = df2
    # print(f(10))




#
#
# f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/(x-x0)
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)
#
# x1 = newton_1(f,df,4,0.01)
# print('Найденный корень: ', x1)
#
#
#
#
# f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/((x-x0)*(x-x1))
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)
#
# x2 = newton_1(f,df,4,0.01)
# print('Найденный корень: ', x2)
#
#
#
#
# f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/((x-x0)*(x-x1)*(x-x2))
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)
#
# x3 = newton_1(f,df,4,0.01)
# print('Найденный корень: ', x3)
#
#
#
#
# f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/((x-x0)*(x-x1)*(x-x2)*(x-x3))
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)
#
# x4 = newton_1(f,df,4,0.01)
# print('Найденный корень: ', x4)
#
#
#
#
# f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/((x-x0)*(x-x1)*(x-x2)*(x-x3)*(x-x4))
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)
#
# x5 = newton_1(f,df,4,0.01)
# print('Найденный корень: ', x5)
#
#
#
#
# f = (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/((x-x0)*(x-x1)*(x-x2)*(x-x3)*(x-x4)*(x-x5))
# df = diff(f,x)
#
# f = lambdify([x], f)
# df = lambdify([x], df)
#
# x6 = newton_1(f,df,4,0.01)
# print('Найденный корень: ', x6)
#
# # здесь он выдает деление на ноль





