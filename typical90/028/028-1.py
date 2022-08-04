import sys
import collections
import math
sys.setrecursionlimit(50000)

MAP = [[0 for i in range(1002)] for j in range(1002)]

n = int(input())
counter = [0 for i in range(n+1)]

for i in range(1,n+1) :
    sx , sy , tx , ty  = map(int,input().split())
    #print(sx , sy , tx , ty)
    for j in range(sx+1,tx+1):
        MAP[j][sy+1] += 1 
        #print ("+1 :", j , sy+1)
    for j in range(sx+1,tx+1):
        MAP[j][ty+1] -= 1
        #print ("-1 :", j , ty+1)


for i in range(1,1002) :
    for j in range(1,1002) :
            MAP[i][j] += MAP[i][j-1]
            counter[MAP[i][j]] += 1

for i in range(1, n+1) : 
    print(counter[i])