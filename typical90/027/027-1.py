import sys
import collections
import math
sys.setrecursionlimit(50000)

n = int(input())
reg = set()

for i in range(1,n+1) :
    a = str(input())
    if a not in reg : 
        reg.add(a)
        print(i)
        