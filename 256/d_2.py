n = int(input())
a = []
for i in range(n):
    l,r = map(int, input().split())
    a.append([l, 0])
    a.append([r, 1])

a = sorted(a)
flag = 0
for i, f in a:
    if f == 0:
        if flag == 0:
            print(i, end = ' ')
        flag += 1
    else:
        flag -= 1
        if flag == 0:
            print(i)
