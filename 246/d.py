n = int(input())

x = 10**14
j = 1000000
for i in range(1001):
    for j in range(1001):
        xx = (i+j) * (i**2 + j**2)
        x = min(xx, x)
        print(x)
        if n < x:
            print(x)
            exit(0)


