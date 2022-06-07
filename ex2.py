import math


def task2(x):
    if x < 20:
        return 52 * (37 * x * x - 85 * x) + 10 * x * x
    elif 20 <= x < 56:
        return x ** 6
    elif x >= 56:
        return 86 * (math.pow(math.floor(x), 4)) - x - 69* math.pow(0.01 - 16 * x ** 3 - 69 * x, 7)


print(task2(141))
