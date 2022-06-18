import math

a, b = map(int, input().split())

c = a**2 + b**2
c = math.sqrt(c)
#print(c)

ac = a/c
bc = b/c
print(ac, bc)