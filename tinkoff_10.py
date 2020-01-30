import math

T = 0

func_n = -2
func_np1 = 0

iter=1
while iter<=2018:

    func_np2 = func_np1 - func_n + (iter**2)

    T = func_np2

    func_n = func_np1

    func_np1 = T


print(T)


