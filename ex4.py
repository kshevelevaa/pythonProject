import math


def main(n):
    if n==0:
        return 0.94
    elif n>=1:
        return 0.01 - math.tan(63-main(n-1)-main(n-1)**3)**2


print(main(3))