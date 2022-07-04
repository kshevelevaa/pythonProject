import math


def main(y):
    if y<173:
        f = y/97 + (y**3/11)**7
    elif 173<=y<270:
        f = y**2 - 3* y**4 -56 * math.cos(y)
    elif y>=270:
        f = math.sqrt(y)**6 - y**2 - 62*(math.abs(y)**3)
    return f


print(main(219))