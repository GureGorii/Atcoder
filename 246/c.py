n, k, x = map(int, input().split())

a = list(map(int, input().split()))
a = sorted(a, reverse=True)
#print(a)

b = []
for i in a:
    m = i // x
    n = i - x*m
    if k >= m:
        k -= m
        b.append(n)
    else:
        n = i - x*k
        b.append(n)
        k = 0
#print(b)

b = sorted(b, reverse=True)
c = []
for i in b:
    if k > 0:
        n = max(0, i - x)
        c.append(n)
        k -= 1
    else:
        c.append(i)

#print(c)
print(sum(c))