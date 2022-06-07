def main(x):
    a=[
        ["RED", 1962, "FISH", x[3]],
        ["DART", 1962, "FISH", x[3]],
        ["RED", 1996, "FISH", x[3]],
        ["DART", 1996, "FISH", x[3]],
        [x[0], 1989, "FISH", 1971],
        [x[0], 1989, "FISH", 2012],
        [x[0], 1989, "FISH", 1969],
        [x[0], x[1], "FANCY", 1971],
        [x[0], x[1], "FANCY", 2012],
        ["RED", x[1], "FANCY", 1969],
        ["DART", x[1], "FANCY", 1969],
        [x[0], x[1], "PAWN", x[3]],
    ]
    for i in range (0, len(a)):
        if a[i]==x:
            return i

print(main(['DART', 1989, 'FANCY', 2012]))
print(main(['DART', 1996, 'FISH', 1969]))
print(main(['RED', 1996, 'PAWN', 1969]))
print(main(['RED', 1996, 'FISH', 1969]))
print(main(['RED', 1989, 'FISH', 1971]))