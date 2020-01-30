import math
from sympy import diff, symbols, lambdify

# возвращает значения функции в точке
x = symbols('x')

def f(x):
    return x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108



def diho(f, a, b, eps):
    quant = 0
    while abs(a - b) > eps:
        x = (a + b)/2.0
        fx = f(x)
        fa = f(a)
        quant += 1
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
            # print("смещаем левую границу в центр\n", x)
        else:
            b = x
            # print("смещаем правую границу в центр\n", x)

    print("кол-во итераций:", quant)
    return x

f1 = x ** 6 - 14 * x ** 5 + 80 * x ** 4 - 238 * x ** 3 + 387 * x ** 2 - 324 * x + 108

f = x ** 6 - 14 * x ** 5 + 80 * x ** 4 - 238 * x ** 3 + 387 * x ** 2 - 324 * x + 108
f = lambdify([x], f)

for i in range(3):

    x0 = diho(f,0.5,4,0.01)
    print('Найденный корень: ', x0)

    f1 = f1/(x-x0)
    print(f1)
    f2 = lambdify([x], f1)

    f = f2

#
# x1 = diho(f, 0.5, 4, 0.1)
# print(x1)
#
# def f1(x):
#     return (x**6 - 14*x**5 + 80*x**4 - 238*x**3 + 387*x**2 - 324*x + 108)/(x-x1)
#
# x2 = diho(f1, 0.5, 4, 0.1)
# print(x2)
#
# def f2(x):
#     return (x ** 6 - 14 * x ** 5 + 80 * x ** 4 - 238 * x ** 3 + 387 * x ** 2 - 324 * x + 108) / ((x - x1)*(x-x2))
#
# x3 = diho(f2, 0.5, 4, 0.1)
# print(x3)
#
# # вот тут
# def f3(x):
#     return (x ** 6 - 14 * x ** 5 + 80 * x ** 4 - 238 * x ** 3 + 387 * x ** 2 - 324 * x + 108) / ((x - x1)*(x-x2)*(x-x3))
#


# уже тут он находит дичь