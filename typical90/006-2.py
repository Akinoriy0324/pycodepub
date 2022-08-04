import sys
import collections
import math
import heapq

sys.setrecursionlimit(50000)

deb = 0

n, k = map(int, input().split())
S = str(input())
SN = [ [ord(moji) - ord('a'), idx] for idx,moji in enumerate(S)]
NEX = [[ -1 for i in range(26)] for j in range(n)]

for i in reversed(range(0,n)):
    letter = SN[i][0]
    NEX[i][letter] = i
    for j in reversed(range(0,i)): 
        if SN[j][0] != letter :
            NEX[j][letter] = i
        else :
            break 

ans = str("")
need = k
prev = -1
##for dat in NEX : print(dat)

while len(ans) < k :
    for i in range(26) :
        if NEX[prev+1][i] == -1 : continue 
        cand = NEX[prev+1][i]
        if n - cand < need : continue 
        ans += S[cand]
        prev = cand
        need -= 1
        break

print(ans)