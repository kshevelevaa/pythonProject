import math


def main(x, y):
    f1 = (55 - 45* (math.cos(y+32*(x**3)))**5)/((1-(59*(x**3) +1 + y**2))**2)
    f2 = x**5 - 36 * (math.exp((x**2)/35 + 54 * y**3))**2
    return f1+f2


print(main(0.44, 0.33))