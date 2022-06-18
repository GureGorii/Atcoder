n = int(input())

a = list(map(int, input().split()))
cnt = 0
if len(a) >= 4:
    for i in range(len(a)-3):
        x = a[i] + a[int(i)+1] + a[int(i)+2] + a[int(i)+3]
        if x >= 4:
            cnt += 1
if 4 <= a[-3] + a[-2] + a[-1]:
    cnt += 1
if 4 <= a[-2] + a[-1]:
    cnt += 1
if 4 <= a[-1]:
    cnt += 1

print(cnt)