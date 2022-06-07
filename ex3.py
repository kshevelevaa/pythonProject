import math


def main(n, m, x):
    res = 0
    f1=1
    for i in range (1, m+1) :
        for c in range (1, n+1):
            f1*=math.pow(i**3 -1 - 8*c*c, 7) + x**12 + math.pow(abs(i), 4)
        res+=f1
        f1 = 1
    return res


print( main(8, 2, -0.73))