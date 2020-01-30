import sympy
import math
from sympy import diff, symbols, lambdify
import numpy as np

x = symbols('x')

class Quadrature:
    """Базовые определения для квадратурных формул"""
    __sum = 0.0
    __nseg = 1  # число отрезков разбиения
    __ncalls = 0 # считает число вызовов интегрируемой функции

    # нужно для сброса констант и подсчета первой итерации
    def __restart(func, x0, x1, nseg0, reset_calls = True):
        """обнуление счетчиков и аккумуляторов
        Возвращает интеграл методом трапеций на начальном разбиении"""
        if reset_calls:
            Quadrature.__ncalls = 0
        Quadrature.__nseg = nseg0
        # вычисление суммы для метода трапеций с начальным разбиением на nseg0 отрезков
        Quadrature.__sum = 0.5 * (func(x0) + func(x1))
        dx = 1.0 * (x1 - x0) / nseg0
        for i in range(1, nseg0):
            Quadrature.__sum += func(x0 + i * dx)

        Quadrature.__ncalls += 1 + nseg0
        return Quadrature.__sum * dx

    def __double_nseg(func, x0, x1):
        """Вдвое измельчает разбиение.
           Возвращает интеграл методом трапеций на новом разбиении"""
        nseg = Quadrature.__nseg
        dx = (x1 - x0) / nseg
        x = x0 + 0.5 * dx
        i = 0
        AddedSum = 0.0
        for i in range(nseg):
            AddedSum += func(x + i * dx)

        Quadrature.__sum += AddedSum
        Quadrature.__nseg *= 2
        Quadrature.__ncalls += nseg
        return Quadrature.__sum * 0.5 * dx

    def romberg(func, x0, x1, rtol = 1e-10, nseg0 = 1, maxcol = 5, reset_calls = True):
        """Интегрирование методом Ромберга
           nseg0 - начальное число отрезков разбиения
           maxcol - максимальный столбец таблицы"""

        i = 0
        U=[[Quadrature.__restart(func, x0, x1, nseg0, reset_calls)]]
        R =[]
        i = 0
        maxcol = max(0, maxcol)
        ans = U[i][i]
        # error_est = max(1, abs(ans))

        # счетчик сгущений
        s = 0


        while (s < maxcol):
            i += 1
            r_p = 4.0
            ans_col = min(i, maxcol)
            U.append([Quadrature.__double_nseg(func, x0, x1)] * (ans_col + 1))

            for j in range(0, ans_col):
                diff = (U[i][j] - U[i - 1][j]) / (r_p - 1.0)
                R.append([diff] * (ans_col))
                U[i][j + 1] = U[i][j] + diff
                r_p *= 16.0

            ans = U[i][ans_col]

            s += 1
            # if (maxcol <= 1):  # метод трапеций обрабатываются отдельно
            #     error_est = abs(ans - U[i - 1][-1])
            # elif (i > maxcol):
            #     error_est = abs(ans - U[i][min(i - maxcol - 1, maxcol - 1)])
            # else:
            #     error_est = abs(ans - U[i - 1][i - 1])

        print("Total function calls: " + str(Quadrature.__ncalls))
        print("матрица решений ", U,"\n")
        print("матрица ошибок ", R, "\n")
        # print("ошибка ", error_est)

        return ans


f = 1/(1+x**2)
f = lambdify([x], f)

integral = Quadrature.romberg(lambda x: 1/(1+x**2),-1.,1.)
print('result is ', integral)