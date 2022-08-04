import sys
from collections import deque
sys.setrecursionlimit(50000)
deb = 0

n = int(input())
tmp = list(map(int, input().split()) )
tmp.sort()
A = tmp[-1]
B = tmp[-2]
C = tmp[-3]

ans = 10**9

q = n//A

for i in range(q,-1,-1) :
    r = (n- A*i)//B 
    for j in range (r,-1,-1) :
        if (n - A*i - B*j) % C == 0  : 
            res = i + j + (n - A*i - B*j) // C
            ans = min(res,ans) 

print(ans)               

