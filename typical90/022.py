import sys
import collections
import math
sys.setrecursionlimit(50000)

deb = 0

A, B, C = map(int, input().split())
Z = math.gcd(math.gcd(A,B),C) 
print (A//Z -1 + B//Z -1 + C//Z -1)

