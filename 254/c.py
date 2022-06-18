n,k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(k):
    a[i::k] = sorted(a[i::k])
if a == sorted(a): print("Yes")
else: print("No")
