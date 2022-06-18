h1, h2, h3, w1, w2, w3 = map(int, input().split())

cnt = 0
for a in range(1, h1-1):
    for b in range(1, h1-a):
        for d in range(1, h2-1):
            for e in range(1, h2-d):
                c=h1-a-b
                f=h2-d-e
                g=w1-a-d
                h=w2-b-e
                i=w3-c-f
                if (g+h+i) == h3 and min({c,f,g,h,i}) > 0:
                    cnt += 1

print(cnt)


