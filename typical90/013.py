import sys
import collections
import math
import heapq

sys.setrecursionlimit(50000)

deb = 0

n, k = map(int, input().split())
MAP = [[] for j in range(n+1)]

for i in range(0,k):
    a, b, c = list(map(int,input().split()))
    MAP[a].append([c, b])
    MAP[b].append([c, a])

def solve(s,g) : 
    CON = [ 0 for j in range(n+1)]
    dist = [ -1 for j in range(n+1)]
    cost = [ -1 for j in range(n+1)]
    Q = []
    for dat in MAP[s] :
        heapq.heappush(Q, dat)
    CON[s] = 1
    dist[s] = 0 
    while Q :
        tmp = heapq.heappop(Q)
        nowcost = tmp[0]
        now = tmp[1]
        if CON[now] > 0 : continue
        CON[now] = 1
        dist[now] = nowcost 
        for dat in MAP[now] :
            tocost = dat[0] + nowcost
            to = dat[1]
            if CON[to] >0 : continue 
            else :
                heapq.heappush(Q, [tocost,to])
    return dist

def main() :
    dist1 = solve(1,-1)
    distn = solve(n,-1)
    for i in range(1,n+1) : 
        #print("1 ->",i," ",solve(1,i))
        #print(i," ->",n," ",solve(i,n))
        print( dist1[i] + distn[i] )

main()