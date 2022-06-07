def main(x):
    a=[
        [x[0], 2008, "MUF", 1975],#0
        [x[0], 1961, "MUF", 1975],#1
        [x[0], 1986, "MUF", 1975],#2
        ["TLA", x[1], "LESS", 1975],#3
        ['E', x[1], "LESS", 1975],#4
        ["NINJA", x[1], "LESS", 1975],#5
        [x[0], 2008, "STON", 1975],#6
        [x[0], 1961, "STON", 1975],#7
        [x[0], 1986, "STON", 1975],#8
        [x[0], x[1], x[2], 1962],#9
    ]
    for i in range (0, len(a)):
        if a[i] == x:
            return i


print(main(['NINJA', 1961, 'MUF', 1962]))#9
print(main(['NINJA', 1961, 'LESS', 1975]))#5
print(main(['E', 1961, 'LESS', 1975]))#4
print(main(['NINJA', 1986, 'STON', 1975]))#8
print(main(['NINJA', 1961, 'MUF', 1975]))#1