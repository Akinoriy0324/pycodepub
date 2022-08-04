import sys
import collections
import math
sys.setrecursionlimit(50000)

##print ( 180 * math.atan(1/math.sqrt(5)) / math.pi )
deb = 0

T = int(input())
L, X, Y = map(int, input().split())
q = int(input())

for i in range(0,q):
    time = int(input())
    y = L/2 * math.cos ( 3 * math.pi / 2 - 2 * math.pi * time / T )
    z = L/2 + L/2 *math.sin ( 3 * math.pi / 2  - 2 * math.pi * time / T )
    x = 0
    distxy = math.sqrt( (x-X)**2 + (y-Y)**2 )
    distz = z - 0 
    print ( 180 * math.atan( distz/distxy) / math.pi )


