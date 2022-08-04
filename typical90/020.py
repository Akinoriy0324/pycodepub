import sys
import collections
import math
sys.setrecursionlimit(50000)

##print ( 180 * math.atan(1/math.sqrt(5)) / math.pi )
deb = 0

a, b, c = map(int, input().split())

if ( a < c**b ) :
    print ("Yes")
else : 
    print ("No")