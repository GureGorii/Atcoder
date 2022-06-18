#入力
x, y, z = map(int,input().split())
s, t = input().split()

## オーバーフロー対策
from decimal import Decimal
n, a, b = map(int,input().split())
n = Decimal(str(n))
a = Decimal(str(a))
b = Decimal(str(b))

## 1次元
n = int(input())
z = list(map(int, input().split()))
#mat = [int(input()) for _ in range(n)]

### それぞれに格納
n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
print(x)
print(y)

## 2次元
#mat = [list(map(int, input().split())) for _ in range(n)]
a = list(list(map(int, input().split())) for i in range(n))

### それぞれに格納
n = int(input())
x = []
y = []
for i in range(n):
    a = list(map(int, input().split()))
    x.append(a)

print(x)

#リスト

## bisectの方が高速
import bisect

n = int(input())
x = {} # 辞書
y = []
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        if a[1] in x:
            x[a[1]]+=1
        else:
            x[a[1]] = 1
            bisect.insort_left(y,a[1])
    elif a[0] == 2:
        if a[1] in x:
          if x[a[1]] > a[2]:
              x[a[1]] -= a[2]
          else:
              del x[a[1]]
              y.pop(bisect.bisect_left(y,a[1]))

## (reverse=True)にすると降順になる
mat = list(map(int, input().split()))
mat.sort(reverse=False) #昇順

mat = list(set(mat)) #重複削除

mat = [1, 1, 4, 5, 1, 4]
print(mat.index(4)) #検索

mat.append(n) #追加
mat.extend(n)
mat.insert(a, n) # aをn番目に挿入
mat.pop(n) # 何もなければ末尾を削除
while 'b' in l:
  l.remove('b') # 要素削除
n = ''.join(mat)


# 辞書
# 生徒の名前
students = ["A", "B", "C"]
# "80 70 90"と入力して、辞書にまとめて代入
scores = {}
for i, score in enumerate(input().split()):
    scores[students[i]] = score
print(scores)

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}
max_d = max(d) # e
min_d = min(d) # a
max_v = max(d.values()) # 100
min_v = min(d.values()) # 100
max_k = max(d, key=d.get) # a
min_k = min(d, key=d.get) # b
max_kv = max(d.items(), key=lambda x: x[1]) # ('a', 100)
min_kv = min(d.items(), key=lambda x: x[1]) # ('a', 100)
max_k, max_v = max(d.items(), key=lambda x: x[1])
print(max_k) # a
print(max_v) # 100

# 組み合わせ
import itertools
N = [1, 2, 3, 4]
## nP2
X = list(itertools.permutations(N))

X = list(itertools.permutations(N, 2))
print(X)

for i in itertools.permutations(N):
  print(list(i))
  
for i in itertools.permutations(N, 2):
  print(list(i))

## nC2
X = list(itertools.combinations(N))

X = list(itertools.combinations(N, 2))
print(X)

for i in itertools.combinations(N):
  print(list(i))
  
for i in itertools.combinations(N, 2):
  print(list(i))