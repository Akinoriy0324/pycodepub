import sys
import re
from collections import deque

sys.setrecursionlimit(100000)
deb = 0
n = int(input())
paths = [[] for i  in range(n+1)]
for i in range(0,n-1) :
    a , b=  map(int, input().split()) 
    paths[a].append(b)
    paths[b].append(a)

#print(paths)
cons = [0 for i in range(n+1)]
dists = [0 for i in range(n+1)]

def doBfs(s):
    Q = deque()
    Q.append(s)
    while Q :
        x = Q[0]
        Q.popleft()
        if cons[x]==2 : continue 
        else :
            cons[x]=2
            for y in paths[x] :
                if cons[y] == 0 :
                    cons[y]=1
                    Q.append(y)
                    dists[y]=dists[x]+1
doBfs(1)

s = dists.index(max(dists))
cons = [0 for i in range(n+1)]
dists = [0 for i in range(n+1)]
doBfs(s)

print(max(dists)+1)
