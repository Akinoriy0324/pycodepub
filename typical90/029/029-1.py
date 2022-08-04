import sys
import collections
import math
sys.setrecursionlimit(50000)
deb = 0
MAP = [[0 for i in range(1002)] for j in range(1002)]

n , q= map(int,input().split())

btm = 0 
while 2**btm <= n :
    btm += 1
N = 2**(btm+1)
if deb : print ("N=",N)

tree = [0 for i in range(N)]
lazy = [0 for i in range(N)]


    
def lazyeval(num) :
    if lazy[num] : 
        tree[num] = lazy[num]
        lazy[num] = 0 
        if (2*num < N) : lazy[2*num] = tree[num]
        if (2*num + 1 < N) : lazy[2*num+1] = tree[num]
    return

def solve(s,g,lt,rt,num):
    if deb : print ("solve",s,g,lt,rt,num)
    if g <= lt or rt <= s : return 0
    lazyeval(num)
    mid = (lt+rt)//2
    if s<= lt and rt <= g : 
        return tree[num]
    return max(solve(s,g,lt,mid,2*num), solve(s,g,mid,rt,2*num+1) )

def update (s,g,lt,rt,num,value):
    if deb : print ("update",s,g,lt,rt,num,value)
    if g <= lt or rt <= s : return 
    lazyeval(num)
    mid = (lt+rt)//2
    if s<= lt and rt <= g : 
        lazy[num] = value
        while num > 1 :
            par = num//2 
            tree[par] = max(tree[par],value)   
            num = par     
        return 
    update(s,g,lt,mid,2*num,value)
    update(s,g,mid,rt,2*num+1, value)
    return

for i in range(1,q+1) :
    s, g  = map(int,input().split())
    if deb : print (s,g)
    val = solve(s,g+1,1,N//2 +1,1) + 1
    print(val)
    update(s,g+1,1,N//2 +1,1,val)
    
    #print(tree)
    #print(lazy)


        