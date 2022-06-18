n = int(input())

a = list(list(map(int, input().split())) for i in range(n))
a = sorted(a)
b = [a[0]]
for i in range(len(a)-1):
    #print(a[i+1])
    if b[0][0] >= a[i+1][1] and b[0][0] <= a[i+1][1]:
        b[0][0] = a[i+1][0]
    elif b[0][1] >= a[i+1][0] and b[0][1] <= a[i+1][1]:
        b[0][1] = a[i+1][1]
    else:
        b.append(a[i+1])
print()
c = [b[0]]
cnt = 1
for i in range(len(b)-1):
    #print(a[i+1])
    for j in range(cnt):
        if c[cnt-1][0] >= b[i+1][1] and c[cnt-1][0] <= b[i+1][1]:
            c[cnt-1][0] = b[i+1][0]
        elif c[cnt-1][1] >= b[i+1][0] and c[cnt-1][1] <= b[i+1][1]:
            c[cnt-1][1] = b[i+1][1]
        else:
            c.append(b[i+1])
            cnt += 1

for i in range(len(c)):
    print(c[i][0], c[i][1])

