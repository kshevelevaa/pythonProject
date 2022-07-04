import math


def main(n):
    if n==0:
        return 0.22
    elif n ==1:
        return -0.44
    elif n>=2:
        return 11* main(n-1)+ 18 * math.sin((main(n-2)))**2 +69


print(main(4))