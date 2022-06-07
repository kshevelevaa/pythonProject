def main(x):
    x=format(x, 'b')
    x = str(x)
    e=x[0:1]
    d=x[1:3]
    c=x[3:8]
    b=x[8:17]
    a=x[17:]
    res = c+a+b+e+d
    return hex(int(res, 2))


print(main(0xd9701d78))


