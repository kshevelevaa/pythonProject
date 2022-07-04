def main(b, n):
    sum = 0
    pr = 1
    for k in range( 1, n+1):
        for j in range ( 1, b+1):
            sum += 82* j**6 - (14*j)**4 - k**3
            pr *= k**2- 0.01-73*j - 55* k**4
    return sum+pr


print(main(7,7))