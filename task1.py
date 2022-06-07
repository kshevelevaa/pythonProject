import math


def main(z):
    answer = math.pow(math.tan(z - 27 * z * z * z - 1), 6) - math.sqrt(40 * math.pow(z, 6) + 56)
    if (z < 92):
        answer = 5
    for i in range(5):
        answer = answer + 1
        answer += main(z - 1)
    return answer


def task5(z):
    answer = 0
    n = len(z)
    for i in range(1, n + 1):
        k = math.ceil(i)  # вверх
        k = math.floor(i)  # вниз
        answer += math.pow(math.pow(z[n + 1 - i], 3) + 1 + 68 * z[n + 1 - i], 7)
        return 64 * answer


def main1(x):
    a = [
        [x[0], "J", 1964, "TCSH"],
        [x[0], "J", 1964, "LIMBO"],
        [x[0], "J", 1964, "NGINX"],
        [x[0], "J", 2003, x[3]],
        [x[0], "LEAN", 1964, "TCSH"]
    ]
    for j in range(len(a)):
        if a[j] == x:
            return j


def main(x):
    print(hex(int('00000000000000000000011111111111', 2)))
    return (x & 0x7FF) << 8 | (x & 0x7800) << 11 | \
           (x & 0x3F8000) >> 15 | (x & 0xC00000) >> 3 | \
           (x & 0xF000000) << 4 | (x & 0x10000000) >> 21 | \
           (x & 0x20000000) >> 8 | (x & 0xC0000000) >> 4

#
#11111111111111111111111111111111
#A
#00000000000000000000011111111111
#B
#00000000000000000111100000000000
#C
#00000000001111111000000000000000
#D
#00000000110000000000000000000000
#E
#00001111000000000000000000000000
#F
#00010000000000000000000000000000
#G
#00100000000000000000000000000000
#H
#11000000000000000000000000000000
print(main(4041046059))

print(main1(['M4', 1977, 'COBOL', 1975, 1974]))
#print(main(5))
