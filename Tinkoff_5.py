import math


# делаем для С(i,j)
# j = int(input("Enter a value for j: "))
# i = int(input("Enter a value for i: "))


# if y == x:
#     print(1)
# elif y == 1:         # see georg's comment
#     print(x)
# elif y > x:          # will be executed only if y != 1 and y != x
#     print(0)
# else:                # will be executed only if y != 1 and y != x and x <= y


i = int(input("Enter a value for i: "))

j=i

summa = 0

while j<=10:

    a1 = math.factorial(j)
    b1 = math.factorial(i)
    c1 = math.factorial(j-i)  # that appears to be useful to get the correct result
    div1 = a1 // (b1 * c1)
    print(div1)

    # for c(10,j)

    a2 = math.factorial(10)
    b2 = math.factorial(j)
    c2 = math.factorial(10-j)  # that appears to be useful to get the correct result
    div2 = a2 // (b2 * c2)
    print(div2)

    K=(-1)**j
    print(K)

    print("////////")

    sum=K*div1*div2

    print("sum=", sum)
    print("iteration number", j)



    summa +=sum

    j +=1

print("summa", summa)