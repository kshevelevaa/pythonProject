def main(x):
    num = format(x, 'b')
    num = str(num)
    while len(num) < 32:
        num = '0' + num
    d = num[0]
    c = num[1:4]
    b = num[4:17]
    a = num[17:]
    res = d +c + a + b
    return hex(int(res, 2))


print(main(0xd76370b7))