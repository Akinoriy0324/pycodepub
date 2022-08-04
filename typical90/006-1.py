import sys
import collections
import math
import heapq

sys.setrecursionlimit(50000)

deb = 0

n, k = map(int, input().split())
S = str(input())
SN = [ [ord(moji) - ord('a'), idx] for idx,moji in enumerate(S)]
#for i in range(n) : 
#    tmp = sum([1 for ele in SN[i+1:n] if ele[0]> SN[i][0] ] )
#    SN[i].append(tmp)
#if deb : print (SN)

ans = str("")
need = k
prev = -1

heapSN = [] 
for data in SN[0:n-k+1] :
    heapq.heappush(heapSN,data)
if deb : print(heapSN)
while True :
    ele = heapq.heappop(heapSN)
    if ele[1] <= prev : 
        continue
    else :
        ans += S[ele[1]]
        prev = ele[1]
        need -= 1
        if (len(ans)==k) : break 
        heapq.heappush(heapSN,SN[n-need])    

print(ans)