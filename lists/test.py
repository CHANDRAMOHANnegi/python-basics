squares = [1, 4, 9, 16, 25]

print(len(squares))



a, b = 0, 1

while a < 1000:
    print(a, end=",")
    a, b = b, a + b
