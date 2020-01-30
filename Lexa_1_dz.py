while n < 5:
    x.append([])
    R.append([])
    p_eff.append([])
    if n == 0:
        m = 3
        x[n].append(tr(a, b, N))
        x[n].append(tr(a, b, r * N))
        x[n].append(tr(a, b, r*r * N))
        R[n].append(0)
        R[n].append((x[n][1] - x[n][0]) / (r * (p_0 + q * n) - 1))
        R[n].append((x[n][2] - x[n][1]) / (r * (p_0 + q * n) - 1))
        p_eff[n].append(0)
        p_eff[n].append(0)
        p_eff[n].append(abs(math.log2(abs(R[n][2] / R[n][1]))))
    while m < 10:
    x[n].append(tr(a, b, pow(r, m) * N))
    R[n].append((x[n][m] - x[n][m-1]) / (r * p_0 - 1))
    p_eff[n].append(abs(math.log2(abs(R[n][m] / R[n][m-1]))))
    m += 1
    n += 1
    else:
    m = 0
    while m < 10:
    if m < n: # смещает n столбец на n строк вниз
    x[n].append(0)
    else:
    x[n].append(x[n-1][m] + R[n-1][m])
    if m < n + 1: # смещает n столбец на n+1 строк вниз
    R[n].append(0)
    else:
    R[n].append((x[n][m] - x[n][m-1]) / (r * (p_0 + q * n) - 1))
    if m < n + 2: # смещает n столбец на n+2 строк вниз
    p_eff[n].append(0)
    else:
    p_eff[n].append(abs(math.log2(abs(R[n][m] / R[n][m-1]))))
    m += 1
    n += 1