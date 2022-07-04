import math


def main (x, y):
    f = 0
    n = len(x)
    for i in range (len(x)):
        k = x[n-1 - math.ceil(i/2)]
        l = y[n-1 - math.ceil(i/2)]**2
        f += 16*(k+l)**7
    return 16*f


print(main([-0.16, 0.1, -0.9, 0.86, 0.55, -0.39],
           [0.93, -0.04, -0.98, -0.29, -0.73, 0.47]))
