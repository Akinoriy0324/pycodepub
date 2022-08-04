n , q = map(int,input().split())
MAP = [[] for j in range(n+1)]

for i in range (0, q) :
    a, b = map(int,input().split())
    MAP[a].append(b)
    MAP[b].append(a)

#  print(MAP)
cnt = 0
for i in range(1,n+1) :
    for j in range(i+1,n+1) :
        for k in range(j+1,n+1) :
            if MAP[i].count(j) and MAP[j].count(k) and MAP[k].count(i) :
                cnt += 1

print(cnt)