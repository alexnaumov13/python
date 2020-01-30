import sympy
import math
from sympy import diff, symbols, lambdify

x = symbols('x')

# def _rectangle_rule(func, a, b, nseg, frac):
#     """Обобщённое правило прямоугольников."""
#     dx = 1.0 * (b - a) / nseg
#     sum = 0.0
#     xstart = a + frac * dx # 0 <= frac <= 1 задаёт долю смещения точки,
#                            # в которой вычисляется функция,
#                            # от левого края отрезка dx
#     for i in range(nseg):
#         sum += func(xstart + i * dx)
#
#     return sum * dx
#
# def midpoint_rectangle_rule(func, a, b, nseg):
#     """Правило прямоугольников со средней точкой"""
#     return _rectangle_rule(func, a, b, nseg, 0.5)
#
# def trapezoid_rule(func, a, b, rtol = 1e-8, nseg0 = 1):
#     """Правило трапеций
#        rtol - желаемая относительная точность вычислений
#        nseg0 - начальное число отрезков разбиения"""
#     nseg = nseg0
#     old_ans = 0.0
#     dx = 1.0 * (b - a) / nseg
#     ans = 0.5 * (func(a) + func(b))
#     for i in range(1, nseg):
#         ans += func(a + i * dx)
#
#     ans *= dx
#     err_est = max(1, abs(ans))
#     while (err_est > abs(rtol * ans)):
#         old_ans = ans
#         ans = 0.5 * (ans + midpoint_rectangle_rule(func, a, b, nseg)) # новые точки для уточнения интеграла
#                                                                       # добавляются ровно в середины предыдущих отрезков
#         nseg *= 2
#         err_est = abs(ans - old_ans)
#
#     return ans

class Quadrature:
    """Базовые определения для квадратурных формул"""
    __sum = 0.0
    __nseg = 1  # число отрезков разбиения
    __ncalls = 0 # считает число вызовов интегрируемой функции

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
        # инициализация таблицы

        Itable = [[Quadrature.__restart(func, x0, x1, nseg0, reset_calls)]]

        # ответ = крайний элемент на диагонали
        i = 0
        maxcol = max(0, maxcol)
        ans = Itable[i][i]
        error_est = max(1, abs(ans))

        while (error_est > abs(rtol * ans)):
            old_ans = ans
            i += 1
            d = 4.0
            ans_col = min(i, maxcol)

            Itable.append([Quadrature.__double_nseg(func, x0, x1)] * (ans_col + 1))

            for j in range(0, ans_col):
                diff = (Itable[i][j] - Itable[i - 1][j]) / (d - 1.0)
                Itable[i][j + 1] = Itable[i][j] + diff
                d *= 4.0

            ans = Itable[i][ans_col]
            if (maxcol <= 1): # метод трапеций обрабатываются отдельно
                error_est = abs(ans - Itable[i - 1][-1])
            elif (i > maxcol):
                error_est = abs(ans - Itable[i][min(i - maxcol - 1, maxcol - 1)])
            else:
                error_est = abs(ans - Itable[i - 1][i - 1])

        print("Total function calls: " + str(Quadrature.__ncalls))
        print("matrix ",Itable)
        return ans

# ввожу функцию f = x^2
f = 1/(1+x**2)
f = lambdify([x], f)

integral = Quadrature.romberg(f,-1.,1.)
print('result is ', integral)