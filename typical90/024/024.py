import sys
import collections
import math
sys.setrecursionlimit(50000)

n, q = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
diff = 0 

for i in range(n) :
    diff += abs(A[i] -B[i])

result = 0 
if diff <= q : 
    if (q - diff) % 2 == 0 :
        result = 1
        
if result :
    print('Yes')
else :
    print('No')
    