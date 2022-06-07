import math


def main(y, x):
    res = 0
    for i in range (len(y)):
        res+=math.sqrt(12-x[i]**3 - y[math.floor(i/2)])**3
    return 38*res


print(main([-0.69, 0.18, -0.71],[-0.62, -0.83, 0.43]))