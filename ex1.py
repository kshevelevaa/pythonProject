import math


def task1(y, x):
    f1 = math.sqrt(69 * math.pow(x + 1, 7) + 52 * math.pow(math.log10(y), 3))
    f2=(math.pow(x, 3) - math.asin(y))
    f3 = ((math.pow(74*x*x+1+20*x*x*x, 7))/43 - 80 * math.pow(math.sin(55 - 71 * y * y), 2))
    return f1-f2/f3


print(task1(0.47, 0.25))
