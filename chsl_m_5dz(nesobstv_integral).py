import sympy
import math
from sympy import diff, symbols, lambdify
import math
x = symbols('x')

f = 2.7182**(-x)
f = lambdify([x], f)


# сделаю программму которая методом средних будет считать этот интеграл на интервале от 0 до бесконечности

def integral_infinity_mid(f, N):
    c = 1
    m = 2
    sum = 0
    for i in range (1, N):
        t = (i - 1/2)/N
        x = c*t/((1-t**2)**m)
        x_diff = c*(1 - ((1 - 2*m)*t**2)) / ((1 - t**2)**(m + 1))
        U_n = (1/N) * f(x) * x_diff
        sum += U_n

    return sum

integral = integral_infinity_mid(f, 10)

print("интеграл равен: ", integral)
# print(f(1))