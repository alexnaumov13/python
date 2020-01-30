# реализуутся интерполяция ряда точек
import matplotlib.pyplot as plt
import numpy as np
import numpy
from sympy import diff, symbols, lambdify


x = symbols('x')

def graph(formula):
    x_1 = np.linspace(min(x_n)*1.1,max(x_n)*1.1,50)
    y_1 = formula(x_1)  # <- note now we're calling the function 'formula' with x
    plt.plot(x_1, y_1)
    plt.show()

x_n = [int(i) for i in input('Введите значения x через пробел ').split()]
y_n = [int(i) for i in input('Введите значения y через пробел ').split()]
print("значения координат x: ", x_n,"\nзначение координат y: ", y_n)

# x_n = [-3, -2, -1, 0, 1, 2, 3, 4]
# y_n = [9, 4, 1, 0, 1, 4, 9, 16]
x_find = input('Введите значения x через пробел ')
x_find = float(x_find)

plt.scatter(x_n, y_n, marker='D', s=7, color='blue')

# нужно переписать метод решения уравнения. Нужно создать матрицу соответствующих значений базисной функции в точках х.
# i - номер строки; j - номер столбца

fi = np.zeros((len(x_n),len(x_n)))

for i in range(len(x_n)):

    for j in range (len(x_n)):
        fi[i][j] = (x_n[i])**j

# numpy.linalg.solve(левая часть системы, правая часть системы)
C = numpy.linalg.solve(fi, y_n)



U = 0
for i in range(len(C)):
    # k = C[i]
    U += C[i]*(x**i)

U = lambdify([x], U)

U_find = U(x_find)

print('Значение функции в заданной точке: ', U_find)
graph(U)